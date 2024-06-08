"""
AIS Plugin for PyTorch

PyTorch Dataset and DataLoader for AIS.

Copyright (c) 2022-2024, NVIDIA CORPORATION. All rights reserved.
"""

from typing import Iterator, List, Union
from torch.utils.data import Dataset, IterableDataset

from aistore.sdk import Client
from aistore.sdk.ais_source import AISSource
from aistore.sdk.dataset.data_shard import DataShard
from aistore.pytorch.utils import (
    list_objects,
    list_objects_iterator,
    list_shard_objects_iterator,
)


class AISBaseClass:
    """
    A base class for creating AIS Datasets for PyTorch.

    Args:
        client_url (str): AIS endpoint URL
        urls_list (Union[str, List[str]]): Single or list of URL prefixes to load data
        ais_source_list (Union[AISSource, List[AISSource]]): Single or list of AISSource objects to load data
    """

    def __init__(
        self,
        client_url: str,
        urls_list: Union[str, List[str]],
        ais_source_list: Union[AISSource, List[AISSource]],
    ) -> None:
        self.client = Client(client_url)
        if isinstance(urls_list, str):
            urls_list = [urls_list]
        if isinstance(ais_source_list, AISSource):
            ais_source_list = [ais_source_list]
        self._objects = list_objects(self.client, urls_list, ais_source_list)


class AISDataset(AISBaseClass, Dataset):
    """
    A map-style dataset for objects in AIS.
    If `etl_name` is provided, that ETL must already exist on the AIStore cluster.

    Args:
        client_url (str): AIS endpoint URL
        urls_list (Union[str, List[str]]): Single or list of URL prefixes to load data
        ais_source_list (Union[AISSource, List[AISSource]]): Single or list of AISSource objects to load data
        etl_name (str, optional): Optional ETL on the AIS cluster to apply to each object

    Note:
        Each object is represented as a tuple of object_name (str) and object_content (bytes)
    """

    def __init__(
        self,
        client_url: str,
        urls_list: Union[str, List[str]] = [],
        ais_source_list: Union[AISSource, List[AISSource]] = [],
        etl_name: str = None,
    ):
        if not urls_list and not ais_source_list:
            raise ValueError(
                "At least one of urls_list or ais_source_list must be provided"
            )
        super().__init__(client_url, urls_list, ais_source_list)
        self.etl_name = etl_name

    def __len__(self):
        return len(self._objects)

    def __getitem__(self, index: int):
        obj = self._objects[index]
        content = obj.get(etl_name=self.etl_name).read_all()
        return obj.name, content


class AISBaseClassIter:
    """
    A base class for creating AIS Iterable Datasets for PyTorch.

    Args:
        client_url (str): AIS endpoint URL
        urls_list (Union[str, List[str]]): Single or list of URL prefixes to load data
        ais_source_list (Union[AISSource, List[AISSource]]): Single or list of AISSource objects to load data
    """

    def __init__(
        self,
        client_url: str,
        urls_list: Union[str, List[str]],
        ais_source_list: Union[AISSource, List[AISSource]],
    ) -> None:
        self.client = Client(client_url)
        if isinstance(urls_list, str):
            urls_list = [urls_list]
        if isinstance(ais_source_list, AISSource):
            ais_source_list = [ais_source_list]
        self.urls_list = urls_list
        self.ais_source_list = ais_source_list
        self._reset_iterator()

    def _reset_iterator(self):
        """Reset the object iterator to start from the beginning"""
        self._object_iter = list_objects_iterator(
            self.client, self.urls_list, self.ais_source_list
        )


class AISIterDataset(AISBaseClassIter, IterableDataset):
    """
    An iterable-style dataset that iterates over objects in AIS.
    If `etl_name` is provided, that ETL must already exist on the AIStore cluster.

    Args:
        client_url (str): AIS endpoint URL
        urls_list (Union[str, List[str]]): Single or list of URL prefixes to load data
        ais_source_list (Union[AISSource, List[AISSource]]): Single or list of AISSource objects to load data
        etl_name (str, optional): Optional ETL on the AIS cluster to apply to each object

    Note:
        Each object is represented as a tuple of object_name (str) and object_content (bytes)
    """

    def __init__(
        self,
        client_url: str,
        urls_list: Union[str, List[str]] = [],
        ais_source_list: Union[AISSource, List[AISSource]] = [],
        etl_name: str = None,
    ):
        if not urls_list and not ais_source_list:
            raise ValueError(
                "At least one of urls_list or ais_source_list must be provided."
            )
        super().__init__(client_url, urls_list, ais_source_list)
        self.etl_name = etl_name
        self.length = None

    def __iter__(self):
        self._reset_iterator()
        for obj in self._object_iter:
            obj_name = obj.name
            content = obj.get(etl_name=self.etl_name).read_all()
            yield obj_name, content

    def __len__(self):
        if self.length is None:
            self._reset_iterator()
            self.length = self._calculate_len()
        return self.length

    def _calculate_len(self):
        return sum(1 for _ in self._object_iter)


class AISMultiShardStream(IterableDataset):
    """
    An iterable-style dataset that iterates over multiple shard streams and yields combined samples.

    Args:
        data_sources (List[DataShard]): List of DataShard objects

    Returns:
        Iterable: Iterable over the combined samples, where each sample is a tuple of
            one object bytes from each shard stream
    """

    def __init__(self, data_sources: List[DataShard]):
        self.data_sources = data_sources

    def __iter__(self) -> Iterator:
        data_iterators = (
            list_shard_objects_iterator(ds.bucket, ds.prefix, ds.etl_name)
            for ds in self.data_sources
        )
        return zip(*data_iterators)
