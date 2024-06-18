Title: Conda
Date: 2017-12-04
Category: Virtual Environments
Slug: conda
Summary: Virtual Environments

### Issues with SSL Cert

```
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org certifi
pip install pip-system-certs
```

### Conda

* `conda create --name <name> python=3.8 -y`
* `conda activate <name>`
* `pip install ipykernel`
* `python -m ipykernel install --user --name=<name>`
* `conda env remove --name <name>`
* `conda env list`
* `conda update`
* `conda install --yes --file requirements.txt`
* `jupyter kernelspec list`
* `conda install --channel=conda-forge nb_conda_kernels`

#### Specific venvs

* Geopandas: `conda create --name=gtfs_graph python=3.8 geopandas scipy --channel=conda-forge`

#### Venv
```
apt-get install python3-venv
python -m venv .env
source .env/bin/activate
```

#### Windows VSC Venv

* To create: `python -m venv .venv`
* To activate: `.venv\Scripts\activate`
  
#### Pipenv

Install

* `sudo apt-get update`
* `sudo apt install python3-pip`
* `pip3 install pipenv`
* `pipenv --python 3.6`

Useful commands

* `pipenv install -r requirements.txt`
* `pipenv shell` to create new env; load/activate existing env, load .env variables
* `pipenv update` can be used to install base dependencies
* `pip install ...`
* `pipenv sync` will use `Pipfile` if present
* `pipenv graph`
