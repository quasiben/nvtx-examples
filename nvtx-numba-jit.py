import nvtx
import numpy as np
from numba import cuda
import math


@cuda.jit
def matmul(A, B, C):
    i, j = cuda.grid(2)
    if i < C.shape[0] and j < C.shape[1]:
        tmp = 0.0
        for k in range(A.shape[1]):
            cuda.syncthreads()
            tmp = tmp + A[i, k] * B[k, j]
        C[i, j] = tmp


np_A = np.random.random((10, 10))
np_B = np.random.random((10, 10))
np_C = np.empty((10, 10), dtype=np.float32)


@nvtx.annotate("copy-to-device", color="purple")
def copy_to_device():
    A = cuda.to_device(np_A)
    B = cuda.to_device(np_B)
    C = cuda.to_device(np_C)
    return A, B, C


A, B, C = copy_to_device()

threadsperblock = (16, 16)
blockspergrid_x = int(math.ceil(A.shape[0] / threadsperblock[0]))
blockspergrid_y = int(math.ceil(B.shape[1] / threadsperblock[1]))
blockspergrid = (blockspergrid_x, blockspergrid_y)

# Start the kernel
with nvtx.annotate("matmul", color="green"):
    matmul[blockspergrid, threadsperblock](A, B, C)

print(C.copy_to_host())
