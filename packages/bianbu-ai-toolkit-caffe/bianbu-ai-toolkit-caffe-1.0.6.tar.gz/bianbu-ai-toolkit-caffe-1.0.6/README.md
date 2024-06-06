## Develop Guide

|  OS  | bianbu_ai_toolkit-x.x.x-py3-none-any.whl |
| ---- | ---- |
| Ubuntu16.04(and above) | Y |
| Centos7.6.1810(and above) | Y |

### bianbu-ai-toolkit

* quick preparation
```bash
$ conda create -n bianbu python=3.8 -y
$ conda activate bianbu
$ pushd toolkit/python
```

* quick setup
```bash
$ python setup.py sdist bdist_wheel --python-tag py38
# quick glance
$ tree bianbu_ai_toolkit.egg-info dist
bianbu_ai_toolkit.egg-info
├── dependency_links.txt
├── entry_points.txt
├── PKG-INFO
├── requires.txt
├── SOURCES.txt
└── top_level.txt
dist
├── bianbu_ai_toolkit-1.0.4-py38-none-any.whl
└── bianbu-ai-toolkit-1.0.4.tar.gz

# other versions
$ python setup.py sdist bdist_wheel --python-tag py39
$ python setup.py sdist bdist_wheel --python-tag py310
$ python setup.py sdist bdist_wheel --python-tag py311
```

* quick install
```bash
$ python -m pip install $(pwd)
```

* quick upload
```bash
# config your ~/.pypirc
$ vi ~/.pypirc
# for example:
[distutils]
index-servers = pypi-bianbu

[pypi-bianbu]
repository: http://nexus.bianbu.xyz/repository/pypi/
username: <username>
password: <password>

# install twine(recommended)
$ python -m pip install twine
# check and upload(tar and wheel ball)
$ python -m twine check dist/*
$ python -m twine upload -r pypi-bianbu dist/*

# another way: upload with setup.py
$ python setup.py sdist bdist_wheel upload -r pypi-bianbu
```

* quick download
```bash
$ python -m pip download bianbu-ai-toolkit --extra-index-url http://nexus.bianbu.xyz/repository/pypi/simple --trusted-host nexus.bianbu.xyz --no-deps
```

#### smoke test

* paddle

```bash
# create user entry point for native python env(if necessary)
ln -sf bianbu bianbu-py
# download paddle2onnx official models
bash dataset/download.sh paddle
# convert paddle to jdsk onnx model
for x in $(find dataset/paddle/*/*/*.pdmodel); do
  echo "[INFO] Convert $x ..." && \
  bianbu convert paddle --model_dir . --model_filename $x --params_filename ${x%.pdmodel}.pdiparams --save_file ${x%.pdmodel}.onnx
done
# smoke test with converted onnx model(with onnxruntime)
for x in $(find dataset/paddle -name "*.onnx"); do
  # add additional `-f` params for segmentation models
  echo "[INFO] Simulation test with $x ..." && \
  bianbu-py simulate --input $x -er 10 -f p2o.DynamicDimension.1:224 p2o.DynamicDimension.2:224
done
```

### caffe2onnx

* quick preparation
```bash
$ conda create -n caffe2onnx python=3.6 -y
$ conda activate caffe2onnx
$ pushd toolkit/python
```

* quick setup
```bash
$ python setup.py caffe2onnx sdist bdist_wheel --python-tag py36
```

* quick install
```bash
$ python -m pip install -r requirements_caffe2onnx.txt
```

* quick test
```bash
# create user entry point for native python env(if necessary)
ln -sf bianbu bianbu-py
# download caffe official models
bash dataset/download.sh caffe
# convert caffe to jdsk onnx model
for x in $(find dataset/caffe/*.caffemodel); do
  echo "[INFO] Convert $x ..." && \
  bianbu convert caffe --input ${x%.caffemodel} --output ${x%.caffemodel}.onnx -v
done
# smoke test with converted onnx model(with onnxruntime)
for x in $(find dataset/caffe -name "*.onnx"); do
  echo "[INFO] Simulation test with $x ..." && \
  bianbu-py simulate --input $x -er 10
done
```

### tf1_to_onnx

* quick preparation
```bash
$ conda create -n tf1_to_onnx python=3.7 -y
$ conda activate tf1_to_onnx
$ pushd toolkit/python
```

* quick setup
```bash
$ python setup.py tf1 sdist bdist_wheel --python-tag py37
```

* quick install
```bash
$ python -m pip install -r requirements_tf1.txt
```

### scripts

```txt
bin
└── bianbu  # As Official Entry Points for Bianbu AI Toolkit
```
