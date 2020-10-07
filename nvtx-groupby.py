import cudf
import nvtx

cdf = cudf.datasets.timeseries()

with nvtx.annotate("agg-all", color="blue"):
    cdf.groupby("name").agg(["count", "mean", "sum"])

with nvtx.annotate("split-agg", color="red"):
    cdf.groupby("name").count(), cdf.groupby("name").mean(), cdf.groupby("name").count()
