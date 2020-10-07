import cudf
import rmm

cdf1 = cudf.datasets.timeseries()
cdf2 = cudf.datasets.timeseries()

gcdf1 = cdf1.groupby("id").mean().reset_index()
gcdf2 = cdf2.groupby("id").mean().reset_index()

gcdf2.join(gcdf1, on=["id"], lsuffix="_l")


rmm.reinitialize(pool_allocator=True, initial_pool_size=2 ** 32)  # 4GBs

gcdf1 = cdf1.groupby("id").mean().reset_index()
gcdf2 = cdf2.groupby("id").mean().reset_index()

gcdf2.join(gcdf1, on=["id"], lsuffix="_l")
