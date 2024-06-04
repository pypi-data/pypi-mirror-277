import timeit
from dataclasses import dataclass

import jax.numpy as jnp
from jax import device_put, jit, random


def dot_product(x: jnp.ndarray, y: jnp.ndarray):
    return jnp.dot(x, y)


jit_dot_product = jit(dot_product)


@dataclass
class Benchmark:
    dim: int
    vector: jnp.ndarray
    query: jnp.ndarray

    def run(self):
        timer = timeit.Timer(
            "dot_product(vector, query)",
            globals={
                "dot_product": jit_dot_product,
                "vector": self.vector,
                "query": self.query,
            },
        )
        n, t = timer.autorange()
        print(
            f"[{self.dim} x {self.vector.dtype}] "
            f"Best of {n} runs: {t * 1e9 / n:.5f} nanoseconds per loop"
        )


def main():
    for dim in (16, 256, 1024, 2048):
        key = random.key(42)
        for dtype in (jnp.float64, jnp.float32, jnp.float16):
            vector = device_put(random.uniform(key, (dim,), dtype=dtype))
            query = device_put(random.uniform(key, (dim,), dtype=dtype))
            Benchmark(dim, vector, query).run()

        for dtype in (jnp.int16, jnp.int8):
            vector = device_put(random.randint(key, (dim,), -127, 128, dtype))
            query = device_put(random.randint(key, (dim,), -127, 128, dtype))
            Benchmark(dim, vector, query).run()


if __name__ == "__main__":
    main()
