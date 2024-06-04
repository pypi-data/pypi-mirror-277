from __future__ import annotations

import warnings

import numpy as np
from sklearn.cluster import MiniBatchKMeans

from approxy.partition import Partition
from approxy.utils import extract_feature, normalize_vector

MAGIC_RANDOM_SEED = 37


class Approxy:
    def __init__(
        self,
        dim: int,
        n_probe: int = 3,
        scale_factor: int = 5,
        auto_index_limit: int | None = None,
    ) -> None:
        """
        Args:
            dim: the dimension of the input vectors.
            n_probe: the number of partitions to be searched.
            scale_factor: scale factor for the top_k during the rough search.
            auto_index_limit: if not None, will build the index automatically when
                the number of vectors reaches the limit.
        """
        self.dim = dim
        self.n_probe = n_probe
        self.scale_factor = scale_factor
        self.auto_index_limit = auto_index_limit

        self.default_partition_num = 64
        self.root_partition = Partition(
            np.empty(0, dtype=int),
            np.empty((0, self.dim)),
            np.empty(0, dtype=int),
        )
        self.partitions: list[Partition] = []
        self.kmeans = MiniBatchKMeans(
            n_clusters=self.default_partition_num,
            init="k-means++",
            random_state=MAGIC_RANDOM_SEED,
        )
        self._indexed = False

    def add(self, vector: np.ndarray):
        if vector.shape != (self.dim,):
            return ValueError(f"the vector dimension doesn't match ({self.dim},)")
        num = self.root_partition.total_num()
        self.root_partition.add(num, normalize_vector(vector))

        if self.auto_index_limit and num >= self.auto_index_limit:
            self.index()

    def index(self, partition_num: int | None = None):
        if self._indexed:
            raise RuntimeError("The index has been built already.")
        if self.root_partition.total_num() == 0:
            raise ValueError("There is no vector to index.")

        self._indexed = True
        if partition_num is None:
            partition_num = int(pow(self.root_partition.total_num(), 1 / 3.14159))

        self.kmeans.set_params(n_clusters=partition_num)
        self.root_partition.incremental_index()
        self.kmeans.fit(self.root_partition.vectors)
        for i in range(partition_num):
            ids = np.where(self.kmeans.labels_ == i)[0]
            partition = Partition(
                ids,
                self.root_partition.vectors[ids],
                self.root_partition.features[ids],
            )
            self.partitions.append(partition)
        self.root_partition.clear()

    def search(self, vector: np.ndarray, top_k: int) -> tuple[np.ndarray, np.ndarray]:
        if vector.shape != (self.dim,):
            raise ValueError(f"the vector dimension doesn't match ({self.dim},)")

        feature = extract_feature(vector)

        if not self.partitions:
            warnings.warn("The index is not built yet.", stacklevel=1)
            ids, vectors = self.root_partition.approximate_search(
                feature, top_k * self.scale_factor
            )
        else:
            center_distances = -np.dot(self.kmeans.cluster_centers_, vector)
            partition_indexes = np.argpartition(center_distances, self.n_probe)[
                : self.n_probe
            ]
            ids_list, vectors_list = [], []
            for index in partition_indexes:
                ids, vectors = self.partitions[index].approximate_search(
                    feature, top_k * self.scale_factor
                )
                ids_list.append(ids)
                vectors_list.append(vectors)

            if self.root_partition.total_num():
                ids, vectors = self.root_partition.approximate_search(
                    feature, top_k * self.scale_factor
                )
                ids_list.append(ids)
                vectors_list.append(vectors)

            ids = np.concatenate(ids_list)
            vectors = np.concatenate(vectors_list)

        if len(ids) <= top_k:
            return ids, vectors
        distances = -np.dot(vectors, vector)
        indexes = np.argpartition(distances, top_k)[:top_k]
        sorted_indexes = sorted(indexes, key=lambda x: distances[x])
        return ids[sorted_indexes], vectors[sorted_indexes]
