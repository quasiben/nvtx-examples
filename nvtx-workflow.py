# 1) General Example of creating + computing
# 2) Continue by analyzing
#  2a) introduce Pool
# 3) Fusion

import cupy
import nvtx
import rmm

# cuda context generation
arr_x = cupy.array(1)


def squared_diff(x, y):
    return (x - y) * (x - y)


# warmup
squared_diff(arr_x, arr_x)
cupy.fuse(squared_diff(arr_x, arr_x))

with nvtx.annotate("data generation", color="purple"):
    imgs = [cupy.random.random((1024, 1024)) for i in range(100)]

with nvtx.annotate("compute", color="yellow"):
    squares = [squared_diff(arr_x, arr_y) for arr_x, arr_y in list(zip(imgs, imgs[1:]))]


cupy.cuda.set_allocator(rmm.rmm_cupy_allocator)
rmm.reinitialize(pool_allocator=True, initial_pool_size=2 ** 32)  # 4GBs

with nvtx.annotate("data generation w pool", color="purple"):
    imgs = [cupy.random.random((1024, 1024)) for i in range(100)]


with nvtx.annotate("compute fast", color="orange"):
    squares = [
        cupy.fuse(squared_diff(arr_x, arr_y))
        for arr_x, arr_y in list(zip(imgs, imgs[1:]))
    ]
