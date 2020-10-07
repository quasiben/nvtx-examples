import multiprocessing
import nvtx

import numpy as np
import time


@nvtx.annotate("mean", color="blue")
def compute_mean(x):
    return x.mean()


@nvtx.annotate("mock generate data", color="red")
def read_data(size):
    return np.random.random((size, size))


def big_computation(size):
    time.sleep(0.5)  # mock warmup
    data = read_data(size)
    return compute_mean(data)


@nvtx.annotate("main")
def main():
    ctx = multiprocessing.get_context("spawn")
    sizes = [4096, 1024]
    procs = [
        ctx.Process(name="calculate", target=big_computation, args=[sizes[i]])
        for i in range(2)
    ]

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()


if __name__ == "__main__":
    main()
