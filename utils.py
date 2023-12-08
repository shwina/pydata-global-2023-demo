import glob
import os
import requests
from tqdm.auto import tqdm


def download(url, fname):
    """
    Download file from `url`, writing the result to `fname`.
    If `fname` already exists, do nothing.
    """
    # this code adapted from the tqdm examples
    # https://github.com/tqdm/tqdm/blob/master/examples/tqdm_requests.py
    if os.path.exists(fname):
        print(f"File {fname} already exists, skipping download")
        return
    response = requests.get(url, stream=True)
    with tqdm.wrapattr(
        open(fname, "wb"),
        "write",
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        miniters=1,
        desc=fname,
        total=int(response.headers.get("content-length", 0)),
    ) as fout:
        for chunk in response.iter_content(chunk_size=4096):
            fout.write(chunk)
            
def download_taxi_data(n):
    """
    Download `n` months of taxi data.
    """
    base = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
    fname = "yellow_tripdata_2021-{i:02d}.parquet"
    url = base + fname
    for i in range(1, n + 1):
        download(url.format(i=i), fname.format(i=i))
