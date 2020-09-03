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

#### Alerts

```python
<div class="alert alert-block alert-info">
case insensitive regexp in str.contains()
</div>
```
