Title: PyPi
Date: 2018-01-01
Category: PyPi
Slug: pypi
Summary: PyPi Code Snippets

#### Pre-requisites

* `pip install -U twine`

* in `~.pypirc` add `chmod 600 ~/.pypirc`


#### Deploy on PyPi

---
**Note**

* Make sure to update version information before deploying. 
Files to update: `__init__.py` and `setup.py`.
* After deploying, don't forget to re-build the documentation at [ReadTheDocs](https://readthedocs.org/projects/shizen-gengo/builds).
---

```
rm -rf build dist && python setup.py sdist
ls dist/*
#python setup.py check -r -s (obolete)
python -m twine check dist/*
python -m  twine upload dist/*
```


#### Misc.

* [Licensing a repository
](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/licensing-a-repository)
