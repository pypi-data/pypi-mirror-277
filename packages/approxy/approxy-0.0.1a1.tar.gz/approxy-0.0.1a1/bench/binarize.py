import timeit
from dataclasses import dataclass
from functools import reduce

import numpy as np


@dataclass
class BenchmarkMod:
    vector: np.ndarray

    def run(self, func):
        timer = timeit.Timer(
            "func(vector)", globals={"func": func, "vector": self.vector}
        )
        n, t = timer.autorange()
        print(
            f"{self.vector.shape} Best of {n} runs for {func.__name__}: {t * 1e6 / n:.5f} microseconds per loop"
        )


def binarize_np(vector: np.ndarray) -> np.ndarray:
    pack = np.packbits(vector >= 0)
    return reduce(lambda x, y: (x << 8) | int(y), pack, 0)


def binarize_py(vector: np.ndarray) -> int:
    return int("".join("1" if x >= 0 else "0" for x in vector), 2)


if __name__ == "__main__":
    for dim in (64, 256, 1024, 2048):
        vector = np.random.rand(dim)
        BenchmarkMod(vector).run(binarize_np)
        BenchmarkMod(vector).run(binarize_py)
