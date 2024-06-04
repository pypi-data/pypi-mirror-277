from __future__ import annotations

import numpy as np

from approxy.utils import extract_feature


class Partition:
    def __init__(
        self, ids: np.ndarray, vectors: np.ndarray, features: np.ndarray
    ) -> None:
        """"""
        self.ids = ids
        self.vectors = vectors
        self.features = features

        # use Python list to accelerate the appending operation
        self.id_list: list[int] = []
        self.vector_list: list[np.ndarray] = []
        self.feature_list: list[int] = []

        if len(self.vectors) != len(self.features):
            raise ValueError("The number of vectors and features should be the same.")

    def total_num(self) -> int:
        return len(self.ids) + len(self.id_list)

    def clear(self):
        self.id_list, self.vector_list, self.feature_list = [], [], []
        dim = self.vectors.shape[1]
        self.ids, self.vectors, self.features = (
            np.empty(0, dtype=int),
            np.array((0, dim)),
            np.empty(0, dtype=int),
        )

    def add(self, pid: int, vector: np.ndarray):
        """Add a new item to this partition."""
        self.id_list.append(pid)
        self.vector_list.append(vector)
        self.feature_list.append(extract_feature(vector))

    def incremental_index(self):
        self.ids = np.concatenate((self.ids, np.array(self.id_list)))
        self.vectors = np.concatenate((self.vectors, np.array(self.vector_list)))
        self.features = np.concatenate((self.features, np.array(self.feature_list)))
        self.id_list, self.vector_list, self.feature_list = [], [], []

    def approximate_search(
        self, feature: int, top_k: int
    ) -> tuple[np.ndarray, np.ndarray]:
        """Search the approximate nearest vectors in the partition."""
        if self.id_list:
            self.incremental_index()
        if not self.total_num():
            return np.array([]), np.array([])
        elif self.total_num() <= top_k:
            return self.ids, self.vectors
        rough_similarities = np.bitwise_xor(self.features, feature)
        indexes = np.argpartition(rough_similarities, top_k)[:top_k]
        return self.ids[indexes], self.vectors[indexes]
