Title: Python
Date: 2018-01-02
Category: Python
Slug: python
Summary: Python Code Snippets

<br>

#### How to Manage API Keys

Pre-requisite: `pip install python-dotenv`

Example config.py: 

```
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(), override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")

# Initialize shared instances
llm_instance = OpenAI(temperature=0, model="gpt-3.5-turbo")
embedding_instance = OpenAIEmbedding(model="text-embedding-ada-002")

llm_instance = OpenAI(temperature=0, model="gpt-4")
embedding_instance = OpenAIEmbedding(model="text-embedding-ada-002")
```

All you have to do then is to import the desired API Key like so:

```
from config import (OPENAI_API_KEY, 
                     PINECONE_API_KEY, 
		     PINECONE_ENV,
       		     llm_instance,
	             embedding_instance)
```

<br>

#### File paths

```
from pathlib import Path

output_dir = Path(__file__).parents[1] / 'data' / 'output'#self.output_dir = Path.cwd() / 'data' / 'output' / 'geojson'

try:
 self.output_dir.mkdir(parents=True, exist_ok=False)
except FileExistsError:
 logger.info('Folder already exists')
else:
 logger.info(f'Folder was created: {self.output_dir}')
```

#### mkdir if not exists

```
from pathlib import Path

TODAY = date.today()
outdir = Path.cwd() / f"outputs/{str(TODAY)}"#.replace('-', '')

if not os.path.exists(outdir):  
  os.makedirs(outdir)
  print("The new directory is created!")
outdir
```

#### limited FOR loop

`for i, elem in zip(range(100), elems[::10])` where `[::10]` is every 10th

#### Query

* `pd.read_csv("file.csv").query("year==2000")`
* `df.query("delay_arrival == 'n/a' | delay_arrival == 'NO_DATA' ")`


#### File Handling: 

```python
with open('filename', 'rb') as f:
    dosomething()
```

```python
# remove if exists then write df to csv
f = 'local-data/filename.csv'
if os.path.isfile(f):
    os.remove(f)
df.to_csv(filepath, sep=',', mode='a', header=False)
```
Notes:

* Opening a file with this statement will handle file closing for you
* The `StringIO` and `cStringIO` modules are gone. 
* Instead, import the `io` module and use `io.StringIO` for **text** and `io.BytesIO` for **data**.
* Calling `read()` reads through the entire file and leaves the read cursor at the end of the file (with nothing more to read).
* Once a file has been read, with `read()` you can use `seek(0)` to return the read cursor to the start of the file
* To check if a file exists or to overwrite an existing file:



#### Get index based on values in another column

```python
id_in_top5 = np.argsort(df_ranked[rank_column][df_ranked[rank_column] <= 5])[::]
```
<br>

### Ranking

#### Create rankings

```python
df['rank'] = df.groupby('source')['dist'].rank(ascending=True)
```

#### Create a dummy rank

This was used for a list of 10 items where 1 to 5 is already ranked and we need to fill the remaining 5 `NaN` ranks with ranks 6 to 10.

```python
def rank2rand(df, col_to_modify):
    counter = it.count(6)
    existing_ranks = np.array(df[[col_to_modify]])
    source = np.array(df[['source_random']])
    updated_ranks = [next(counter) if y == 1 else sum(x) for x, y in zip(existing_ranks, source)]
    return updated_ranks
```

<br>

### Lambda

```python
def transform():
    return lambda x: 2**x
f = transform()
print(f(-2))
```
see also [Lambda, filter, reduce and map](https://www.python-course.eu/python3_lambda.php)

#### Lambda and dataframes: examples

`df = df.apply(lambda x: x.astype(str).str.upper())`

`df['Score'] = df['Score'].apply(lambda x: sigmoid(float(x)))`

`df['string_id'] = df['string_id'].apply(lambda id_string: '9606.' + id_string)`

<br>

### Misc.

#### *args & **kargs

* *args refers to an undetermined number of positional arguments
* **kargs refers to an undetermined number of keyword arguments

```
def add_numbers(num0, num1, num2=2, num3=3):
	outcome = num0 + num1 + num2 + num3
	print(f"num0={num0}, num1={num1}, num2={num2}, num3={num3}")
    return outcome
```

[read more](https://medium.com/better-programming/top-5-mistakes-you-make-when-declaring-functions-in-python-b7a0747711a4)


#### Remove zeros from numpy array

```python
index = np.where(y_pred == 0)[0]
    # print(index)
    y_true = np.delete(y_true, index)
    y_pred = np.delete(y_pred, index)
```

see also [Top 4 Numpy Functions You Don’t Know About](https://towardsdatascience.com/top-4-numpy-functions-you-dont-know-about-probably-28fcd5d7174f)

#### double colon e.g. `[::3]`

`[::3]` just means that you have not specified any start or end indices for your slice (as in `seq[start:end:step]`).

 Since you have specified a step, 3, this will take every third entry of something starting at the first index.

For example: `'123123123'[::3] >> '111'`

It can also be used to reverse a list using `[::-1]`:

`a[::-1]` does not reverse anything, it's just a new view on the same data, more specifically a mirror view.

 The method `a[::-1].sort()` operates on the mirrored image, implying that when sort moves left a smaller item in its
 mirrored image, in reality it is moving it to the right in the real memory block of the a array. The mirrored view is
 sorted in ascending order, the real data is sorted in descending order.
 [source](https://stackoverflow.com/questions/26984414/efficiently-sorting-a-numpy-array-in-descending-order)

#### What does selection by `[:,None]` do?

```python
>>>> import numpy as NP
>>>> a = NP.arange(1,5)
>>>> print a
[1 2 3 4]
>>>> print a.shape
(4,)
>>>> print a[:,None].shape
(4, 1)
>>>> print a[:,None]
[[1]
 [2]
 [3]
 [4]]
```
see also [here](http://stackoverflow.com/questions/37867354/in-numpy-what-does-selection-by-none-do)


#### About Relative Imports

* In order to run a script that uses relative imports such as `from .build_corpus import BuildCorpus`,
you must run the script from the **parent** directory using `-m` and **without** the `.py`
e.g. `python -m cai_pytorch.pytorch`


#### About Python Modules


* When getting error: `module ... not found`: [see here](http://askubuntu.com/questions/470982/how-to-add-a-python-module-to-syspath)
* To prevent getting error `no module named...` resp. before importing a module from a different project make sure to run: 
`$ python setup.py install`
* How to get `import` of modules to work ([source](http://stackoverflow.com/questions/36650163/cant-import-from-specific-folder-in-pycharm))
* Modules are imported from a Python Package, not from a Directory. Therefore, instead of storing python scripts in a    directory, store them in a Python Package: right-click on your project directory, choose Python Package.
* Alternatively, in the existing directory, create an empty `__init__.py` file.


#### About Python Packages

To list installed packages

```python
import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)
```

#### Python Profiler for Debugging

* [cProfiler](https://stackoverflow.com/questions/49262187/storing-the-link-prediction-score-in-a-matrix-form-using-networkx)

* line profiler

  Assumes you are using a shell script to run your program.

  Pre-requiste: `pip install line_profiler`

  1. change shell script as follows:

           #!/bin/bash -x

           kernprof -lv my_script.py \
           # time python3 my_script.py \
           ...

  2. add `@profile` at the start of each function you want to profile

  3. execute shell script

  4. when done, reverse changes made in Steps 1. and 2.


#### `super()` with `__init__()`
  
[Understanding Python super() with __init__() methods](https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods)

#### About the Python import mechanism

* [here](https://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py)
* [and here](https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python)

#### Time it

time a for loop:

```
%%timeit -n 10
for ...:
  ...
```
           
general timing

```
testtime = datetime.now()
...
testtime = testtime.strftime("%H:%M")

```

```
import time
t0 = time.time()
...
t1 = time.time()
t2r = t1 - t0
print('execution time {:.4f} mins'.format(t2r / 60))
```

#### Logging & Try/Except

* [A Comprehensive Guide to Handling Exceptions in Python](https://medium.com/better-programming/a-comprehensive-guide-to-handling-exceptions-in-python-7175f0ce81f7)

```python
def build_pathway_dataset(self, list-of-args, **kwargs):
    logger = logging.getLogger(self.__class__.__qualname__)
    try:
        if pathway:
            logger.info('Building Pathway Data Set')
            t0 = time.time()
            dataset = PathwayDataset(list-of-args)
            dataset.build(pathway_limit=pathway_limit)
            t1 = time.time()
            logger.info('finished in %5.2f s', t1-t0)
        else:
            logger.info('dataset will not be built')
    except Exception as e:
        logger.exception('\n'.join(traceback.format_exception(type(e), e, sys.exc_info()[2])))
        raise e
```


#### Create a temporary file for unit tests:

```python
from tomoe.io import get_tomoe_local_data_dir
import tempfile
temp_path = tempfile.mkdtemp(suffix="dist-graph-sampling")

 ...

TOMOE_TEMP_FOLDER = get_tomoe_local_data_dir()

 ...
triples_hg_csv_path = os.path.join(temp_path, 'triples.hg.csv.tsv')
triple_csv_to_hyperedge_csv(triples_csv_path, triples_hg_csv_path)
assert os.stat(triples_hg_csv_path).st_size != 0
```

#### Variable assignemnt Gotchas

```python
a=list(range(5))
print(a)
b=a
print(b)
a[2]=12
print(b)
```

#### How to install Python 3.6 on Ubuntu 16.04 LTS

```sh
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
```
may be needed:

`sudo apt-get install python3.6-gdbm` 

#### Convert Python2 to Python3

```sh
pip install 2to3
2to3 -n -w path/to/script/script_namae.py
```

Note: `-n` prevents backup files; `-w` instructs to write the conversion

#### SSLCert Error

```
import requests
from requests.sessions import Session
from requests.adapters import HTTPAdapter

# Original function
original_send = HTTPAdapter.send

def patched_send(self, request, **kwargs):
    kwargs['verify'] = False  # Disable SSL verification
    return original_send(self, request, **kwargs)

# Patch the send method
HTTPAdapter.send = patched_send
```

`pip install --trusted-host pypi.org -r .\requirements.txt`

<br>

#### Misc

* `strip()` strips off the new line character
* Widen Pycharm console output for pandas DFs: `pd.set_option('display.expand_frame_repr', False)`
* About `action="store_true"`: [see here](https://docs.python.org/2/howto/argparse.html)
* `PYTHONPATH` is the module search path.
* `PYTHONHOME` is used for the standard libraries,


#### Various Links

* [Python regular expressions](http://zetcode.com/python/regularexpressions/)
* [Weird Python Integers](https://kate.io/blog/2017/08/22/weird-python-integers/)
* [json.dumps vs json.loads](https://stackoverflow.com/questions/34229363/converting-json-string-into-python-dictionary)
* [py joblib tutorial](https://joblib.readthedocs.io/en/latest/) ( about parallelization )
* [Top 10 Nice-To-Have Data Science Libraries](https://medium.com/analytics-vidhya/top-10-nice-to-have-data-science-libraries-d155196710ef)
* [How to analyse 100 GB of data on your laptop with Python](https://towardsdatascience.com/how-to-analyse-100s-of-gbs-of-data-on-your-laptop-with-python-f83363dda94)
* [Kaggle Learn](https://www.kaggle.com/learn/overview)
* [Tips and Tricks for Handling Configuration Files in Python](https://medium.com/better-programming/tips-and-tricks-for-handling-configuration-files-in-python-a9d7429aa50b)
* [Don’t Fear the Pickle: Using pickle.dump and pickle.load](https://medium.com/better-programming/dont-fear-the-pickle-using-pickle-dump-and-pickle-load-5212f23dbbce)
* [Python Videos](https://www.youtube.com/channel/UCFxcvyt2Ucq5IL0_1Njzqlg/playlists)
* [15 Data Science Books You Should Read](https://towardsdatascience.com/15-data-science-books-you-should-read-6f6981e6b3d8)
* [Computational Statistics in Python](https://people.duke.edu/~ccc14/sta-663/index.html)
* [What Are *args and **kwargs in Python?](https://medium.com/better-programming/what-are-args-and-kwargs-in-python-6aaf9e3cad73)
* [Introduction to Functional Programming in Python](https://medium.com/better-programming/introduction-to-functional-programming-in-python-3d26cd9cbfd7) ( about __call__() )
* [Making Python Programs Blazingly Fast](https://towardsdatascience.com/making-python-programs-blazingly-fast-c1cd79bd1b32)
* [Decorators and Functions in Python](https://levelup.gitconnected.com/handy-python-features-e33751ef98a8)
* [Decorators in Python](https://medium.com/better-programming/decorators-in-python-72a1d578eac4)
* [Statistics in Python](https://www.statsmodels.org/stable/index.html)
* [create iterators in a very pythonic manner](https://towardsdatascience.com/reduce-memory-usage-and-make-your-python-code-faster-using-generators-bd79dbfeb4c)
* [Descriptive Statistics with Python](https://medium.com/dataseries/descriptive-statistics-with-python-75e2b1249e8d)

