# cudf.pandas - PyData Global 2023 Demo

## Resources

- [Try cudf.pandas now](https://nvda.ws/rapids-cudf): Explore `cudf.pandas` on a free GPU enabled instance on Google Colab!
- [Install](https://docs.rapids.ai/install): Instructions for installing cuDF and other [RAPIDS](https://rapids.ai) libraries.
- [cudf (Python) documentation](https://docs.rapids.ai/api/cudf/stable/)
- [libcudf (C++/CUDA) documentation](https://docs.rapids.ai/api/libcudf/stable/)
- [RAPIDS Community](https://rapids.ai/learn-more/#get-involved): Get help, contribute, and collaborate.

## Install cuDF and other requirements

These are the quick install instructions for CUDA 11/12.
For detailed instructions, go to https://rapids.ai/#quick-start


To install the stable version of cuDF:

```
pip install cudf-cu11 --extra-index-url=https://pypi.nvidia.com  # or cu-12
```


To install the latest nightly build:

```python
pip install -i https://pypi.anaconda.org/rapidsai-wheels-nightly/simple cudf-cu11  # or cu-12
```

Some other libraries you'll need to install:

```
pip install requests seaborn tqdm
pip install langchain
pip install langchain-experimental
```

## Download the data

There's a helper script to download the data you need for this demo:

```python
from utils import download_taxi_data
download_taxi_data(n=12)
```
