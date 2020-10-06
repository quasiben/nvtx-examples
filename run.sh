nsys profile -t nvtx,osrt --force-overwrite=true --stats=true --output=quickstart.qdrep python nvtx-quickstart.py 

nsys profile -t nvtx,cuda --force-overwrite=true --stats=true --output=numba-jit python nvtx-cuda-jit.py 
nsys profile -t nvtx,cuda --force-overwrite=true --stats=true --output=cudf-groupby python nvtx-groupby.py 

nsys profile -t nvtx,cuda --force-overwrite=true --stats=true --output=cupy python nvtx-cupy.py 
nsys profile -t nvtx,cuda --force-overwrite=true --stats=true --output=workflow python nvtx-workflow.py 
MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nsys profile -t nvtx,osrt,cuda --stats=true --force-overwrite=true --output=multiprocessing python nvtx-multiprocess.py 