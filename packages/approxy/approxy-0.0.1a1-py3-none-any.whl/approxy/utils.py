from __future__ import annotations

from functools import reduce

import numpy as np


def normalize_vector(vector: np.ndarray) -> np.ndarray:
    """Normalize the input vector."""
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    return vector / norm


def extract_feature(vector: np.ndarray) -> int:
    """Extract the binary feature from the vectors."""
    pack = np.packbits(vector >= 0)
    return reduce(lambda x, y: (x << 8) | int(y), pack, 0)
