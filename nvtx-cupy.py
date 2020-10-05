import cupy
import nvtx



# cuda context generation
arr_x = cupy.array(1)

def squared_diff(x, y):
    return (x - y) * (x - y)

# warmup
squared_diff(arr_x, arr_x)
cupy.fuse(squared_diff(arr_x, arr_x))


with nvtx.annotate("square-diff", color="green"):
    with nvtx.annotate("data generation", color="purple"):
        arr_x = cupy.arange(100)

    with nvtx.annotate("copy", color="blue"):
        arr_y = arr_x.copy()[::-1]

    with nvtx.annotate("compute", color="yellow"):
        squared_diff(arr_x, arr_y)

    with nvtx.annotate("faster compute", color="orange"):
        cupy.fuse(squared_diff(arr_x, arr_y))

