Title: Jupyter Notebooks
Date: 2018-01-05
Category: Python
Slug: Jupyter Notebooks
Summary: Jupyter Notebooks

<br> 

#### Useful Links

* [Integrate JupyterLab with Google Drive](https://towardsdatascience.com/integrate-jupyterlab-with-google-drive-98d13e340c63)
* [How to Setup Your JupyterLab Project Environment](https://towardsdatascience.com/how-to-setup-your-jupyterlab-project-environment-74909dade29b)
*[Interactive Controls in Jupyter Notebooks](https://towardsdatascience.com/interactive-controls-for-jupyter-notebooks-f5c94829aee6)
* [Changing JupyterLab to suit your needs](https://www.youtube.com/watch?v=a9P7qv4P5LE)
* <http://localhost:8888/tree#nbextensions_configurator  >

<br>

#### Making Jupyter available on HOST browser

`jupyter lab --ip=0.0.0.0`

* [Running Jupyter Notebooks on a Ubuntu Server](https://hackersandslackers.com/running-jupyter-notebooks-on-a-ubuntu-server/)
* [access jupyter notebook running on vm](https://stackoverflow.com/questions/38545198/access-jupyter-notebook-running-on-vm)
* [Can't access jupyter notebook in local vagrant virtualbox via local browser](https://stackoverflow.com/questions/47597515/cant-access-jupyter-notebook-in-local-vagrant-virtualbox-via-local-browser)

#### Installing IPywidgets

* **make sure notebook is trusted**

```powershell
conda install -c conda-forge nodejs
pip install jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --sys-prefix
python -m ipykernel install --user --name=myEnv
jupyter nbextension enable --py widgetsnbextension
jupyter labextension list
```

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
