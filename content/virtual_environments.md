Title: Virtual Environemnts
Date: 2017-12-04
Category: Virtual Environemnts
Slug: Virtual Environemnts
Summary: Virtual Environemnts


#### Conda

* `conda create --name <name> python=3.7`
* `conda env remove --name <name>`
* `conda env list`
* `conda activate <name>`
* `conda update`
* `conda install --yes --file requirements.txt`
* `conda install -c anaconda ipykernel`
* `python -m ipykernel install --user --name <name>`

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