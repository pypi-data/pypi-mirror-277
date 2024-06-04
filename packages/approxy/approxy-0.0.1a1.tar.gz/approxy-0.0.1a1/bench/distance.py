import timeit
from dataclasses import dataclass
from random import randint

import numpy as np


def dot_product(x: np.ndarray, y: np.ndarray):
    return np.dot(x, y)


def hamming(x: np.ndarray, y: np.ndarray):
    diff = np.bitwise_xor(x, y)
    return sum(x.bit_count() for x in diff)


def bit_xor_count(x: int, y: int):
    return (x ^ y).bit_count()


@dataclass
class Benchmark:
    dim: int
    vector: np.ndarray
    query: np.ndarray

    def run(self, func):
        timer = timeit.Timer(
            "dot_product(vector, query)",
            globals={
                "dot_product": func,
                "vector": self.vector,
                "query": self.query,
            },
        )
        n, t = timer.autorange()
        print(
            f"[{self.dim} x {self.vector.dtype if isinstance(self.vector, np.ndarray) else type(self.vector)}]({func.__name__}) "
            f"Best of {n} runs: {t * 1e9 / n:.5f} nanoseconds per loop"
        )


def generate_int(dim):
    return int("".join(str(randint(0, 1)) for _ in range(dim)), 2)


def main():
    for dim in (16, 256, 1024, 2048):
        for dtype in (np.float64, np.float32, np.float16):
            vector = np.random.rand(dim).astype(dtype)
            query = np.random.rand(dim).astype(dtype)
            Benchmark(dim, vector, query).run(dot_product)

        for dtype in (np.int16, np.int8):
            vector = np.random.randint(-127, 128, dim).astype(dtype)
            query = np.random.randint(-127, 128, dim).astype(dtype)
            Benchmark(dim, vector, query).run(dot_product)

        for dtype in (np.uint64, np.uint32, np.uint16, np.uint8):
            vector = np.random.randint(0, 256, dim).astype(dtype)
            query = np.random.randint(0, 256, dim).astype(dtype)
            Benchmark(dim, vector, query).run(hamming)

        vector, query = generate_int(dim), generate_int(dim)
        Benchmark(dim, vector, query).run(bit_xor_count)


if __name__ == "__main__":
    main()
