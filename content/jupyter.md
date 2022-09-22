Title: Jupyter
Date: 2018-01-05
Category: Python
Slug: jupyter
Summary: Jupyter Notebooks

<br> 

`jupyter lab --ip=0.0.0.0`

`jupyter notebook --ip=0.0.0.0`

#### Import notebook into another
```
pip install jupyter-helpers
from create_gtfs_feed import Feed where create_gtfs_feed is a notebook
```

#### Share variables / objects across notebooks

%store G >> to store
%store -r G >> to load


#### Dill (similar to Pickle)

```
# Dump graph
with open("multigraph.p", 'wb') as f:
    dill.dump(G, f)
```
```
# Load graph
with open("multigraph.p", 'rb') as f:  # notice the r instead of w
    G = dill.load(f)
```

#### Installing Jupyterlab

```powershell
pip install jupyterlab
pip install jupyterlab-widgets
```

#### Installing IPywidgets

With Conda
```powershell
conda install -c conda-forge nodejs -y &&
conda install -c conda-forge jupyterlab -y &&
jupyter labextension install @jupyter-widgets/jupyterlab-manager &&
jupyter contrib nbextension install --sys-prefix
```

With Pip
```
pip install jupyter_contrib_nbextensions
```

* `python -m ipykernel install --user --name=myEnv`
* `jupyter nbextension enable --py widgetsnbextension`
* `jupyter labextension list`
* to launch: `jupyter-lab`


#### Installing Jupyter Lab Extensions

```
jupyter labextension install @jupyterlab/toc
jupyter labextension install @jupyterlab/plotly-extension
```
for plotly see [here](https://stackoverflow.com/questions/54936125/plotly-gives-an-empty-field-as-output-in-jupyter-lab) for more.


#### Converting Notebook to PDF or HTML

Pre-requisites:

`sudo apt-get install texlive texlive-xetex texlive-latex-extra texlive-generic-extra pandoc`

Conversion:

`jupyter nbconvert --to html features_applied.ipynb --TemplateExporter.exclude_input=True`


#### Alerts

```python
<div class="alert alert-block alert-info">
case insensitive regexp in str.contains()
</div>
```

#### Useful Links

* [Integrate JupyterLab with Google Drive](https://towardsdatascience.com/integrate-jupyterlab-with-google-drive-98d13e340c63)
* [How to Setup Your JupyterLab Project Environment](https://towardsdatascience.com/how-to-setup-your-jupyterlab-project-environment-74909dade29b)
* [Interactive Controls in Jupyter Notebooks](https://towardsdatascience.com/interactive-controls-for-jupyter-notebooks-f5c94829aee6)
* [Changing JupyterLab to suit your needs](https://www.youtube.com/watch?v=a9P7qv4P5LE)
* [localhost:8888/tree#nbextensions_configurator](http://localhost:8888/tree#nbextensions_configurator)
* [Running Jupyter Notebooks on a Ubuntu Server](https://hackersandslackers.com/running-jupyter-notebooks-on-a-ubuntu-server/)
* [access jupyter notebook running on vm](https://stackoverflow.com/questions/38545198/access-jupyter-notebook-running-on-vm)
* [Can't access jupyter notebook in local vagrant virtualbox via local browser](https://stackoverflow.com/questions/47597515/cant-access-jupyter-notebook-in-local-vagrant-virtualbox-via-local-browser)
