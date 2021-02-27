Title: Pandas NLP
Date: 2018-01-26
Category: Python
Slug: python, pandas, nlp
Summary: Pandas NLP

#### Useful Links

* [NLTK RegexpParser, chunk phrase by matching exactly one item](https://stackoverflow.com/questions/39124492/nltk-regexpparser-chunk-phrase-by-matching-exactly-one-item)
* [TextHero: The Absolute Simplest way to Clean and Analyze Text in Pandas](https://towardsdatascience.com/try-texthero-the-absolute-simplest-way-to-clean-and-analyze-text-in-pandas-6db86ed14272)
* [shizen-gengo](https://pypi.org/project/shizen-gengo/)


### Imports

```python
import io
import unicodedata
import re
from functools import reduce

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer() 
tokenizer = RegexpTokenizer(r'\w+')
words = set(stopwords.words("english")) # set() sppeds up stopword removal!!

```

### SpaCy

`$ python3 -m spacy download en_core_web_sm`

### NLTK

once off download required. from cmd, launch python and run:

```python
import nltk
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)
```

#### NLTK Grammars

```python
grammar = "NP: {(<V\w+>|<NN\w?>)+.*<NN\w?>}" 
grammar = "NP: {<DT>?<JJ|NN|V><V|NN|NNS|NNP>+}"
grammar = r"""
  NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
  {<NNP>+}                # chunk sequences of proper nouns
  {<NN>+}                 # chunk consecutive nouns
  """
```

### Regexp

#### Regexp String Matching

```Regexp
col         = 'category'
conditions  = [(tmp[col].str.contains("(?i)ISD")),
               (tmp[col].str.contains("(?i)DST")),
               tmp[col].str.contains("(?i)IT")
              ]
choices     = ['ISD', 'DST', 'IT']

tmp["category_high_level"] = np.select(conditions, choices, default=tmp.category)
tmp.stb.freq(['category_high_level']).set_index('category_high_level')
```

#### Sentence Fragement by Word Window

```Regexp
pat = '(?P<before>(?:\w+\W+){,3})products\W+(?P<after>(?:\w+\W+){,3})'
new = df.text.str.extract(pat, expand=True)
df.assign(**new)
```

### Misc.

#### Extract words from a list 

`df['named_entities'] = [','.join(map(str, l)) for l in df['named_entities']]`



