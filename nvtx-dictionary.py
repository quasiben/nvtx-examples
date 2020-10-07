# requires 3.8.5 source build and nvtx patch

# nvtx-dictionary-cpython.patch
# git clone git@github.com:python/cpython.git
# cd cpython
# git checkout v3.8.5
# git apply nvtx-dictionary-cpython.patch
# ./configure --prefix=$CONDA_PREFIX
# C_INCLUDE_PATH=$CONDA_PREFIX/include make -j install

A = {"a": 1}

for i in range(10 ** 10):
    A["a"]


# Generating Operating System Runtime API Statistics...
# Operating System Runtime API Statistics (nanoseconds)

# Time(%)      Total Time       Calls         Average         Minimum         Maximum  Name
# -------  --------------  ----------  --------------  --------------  --------------  --------------------------------------------------------------------------------
#    45.6          112189          26          4315.0            1000           21248  read
#    33.3           82017          17          4824.5            3085            5916  open64
#    10.7           26281           6          4380.2            3446            5077  mmap64
#     6.1           15126           3          5042.0            3465            7582  fopen64
#     1.3            3128           2          1564.0            1157            1971  sigaction
#     1.1            2752           1          2752.0            2752            2752  fread
#     0.7            1768           1          1768.0            1768            1768  fclose
#     0.6            1505           1          1505.0            1505            1505  getc
#     0.5            1325           1          1325.0            1325            1325  dup


# Generating NVTX Push-Pop Range Statistics...
# NVTX Push-Pop Range Statistics (nanoseconds)

# Time(%)      Total Time   Instances         Average         Minimum         Maximum  Range
# -------  --------------  ----------  --------------  --------------  --------------  -------------------
#    95.1         2047054        5069           403.8              89          314968  PyObject-GetAttr
#     4.9          106050         372           285.1             112             782  member-get
