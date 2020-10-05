import time
import nvtx

@nvtx.annotate(color="purple")
def f():
    for i in range(5):
        with nvtx.annotate("loop", color="red"):
            time.sleep(i)

f()
