Title: Pandas Applied
Date: 2018-01-25
Category: Python
Slug: python, pandas
Summary: Pandas Applied

#### Useful Links

* [inter-annotator agreement](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html)

### Sentence Fragment: Search Window with RegExp

```python
def search_window(dataframe_col, token = ''):
    if dataframe_col.ndim == 1:
        raise Exception ("not a dataframe")
    print(len(dataframe_col))
    dataframe_col.replace("", np.nan, inplace=True)
    dataframe_col = dataframe_col.dropna()
    print(len(dataframe_col))
    pat = r'(?P<before>(?:\w+\W+){,8})(?i)' + token + r'\W+(?P<after>(?:\w+\W+){,8})'
    res = dataframe_col.str.extract(pat, expand=False)
    res = res.dropna()
    # print(len(new))
    return res.sample(min(10, len(res)))
```

### Inter-annotator agreement

```
Unit    obs1    obs2    obs3    obs4    obs5
1       1       1       2       .       2
2       1       1       0       1       .
3       2       3       3       3       .
4       .       0       0       .       0
5       0       0       0       .       0
6       0       0       0       .       0
7       1       0       2       .       1
```

#### Reshape data to triples in the form `(coder,item,label)`

```python
df = pd.DataFrame()
for index, row in other_df.iterrows():
    df = df.append({'coder': 'obs_1', 'item': index, 'label': row['obs1']}, ignore_index=True)
    df = df.append({'coder': 'obs_2', 'item': index, 'label': row['obs2']}, ignore_index=True)
    df = df.append({'coder': 'obs_3', 'item': index, 'label': row['obs3']}, ignore_index=True)
    df = df.append({'coder': 'obs_4', 'item': index, 'label': row['obs4']}, ignore_index=True)
    df = df.append({'coder': 'obs_5', 'item': index, 'label': row['obs5']}, ignore_index=True)
print(df)
```

```python
import os
import itertools
import pandas as pd
import numpy as np
from sklearn.metrics import cohen_kappa_score
files = os.listdir(input_eval_dp)
for file, type in itertools.product(files, type_label_list):
    fp = os.path.join(input_eval_dp, file)
    eval_df = get_eval(fp)
    eval_typed_df = eval_df[eval_df['type'] == type]

    # remove any rows where at least one NA is found
    eval_typed_df = eval_typed_df.dropna(subset=['judge_1', 'judge_2'])

    # transform the three columns with scores into a 15 x 3 matrix
    rankings = eval_typed_df.iloc[:, -3:-1].astype(int).as_matrix()

    judge_A_matrix = rankings[:, 0]
    judge_B_matrix = rankings[:, 1]

    # Kappa Cohen 2 annotators
    print("\n'{}'\tinter annotator agreement between judge A and judge B".format(type))
    cohen_kappa(judge_A_matrix, judge_B_matrix)
```


### DataFrame.apply 

df_a
```
   ent_a  count
0   5197    1.0
1  12766    2.0
2   3091    2.0
3   3162    1.0
4   1956   13.0
```

df_ab
```
       ent_ab  count_ab
0   5197-56744       1.0
1   12766-5197       1.0
2  12766-56744       1.0
3    3091-3162       1.0
4   3091-54583       1.0
```

#### Add column:

`df_ab['ent_a'] = df_ab.ent_ab.apply(lambda x: x.split('-')[0])`


df_ab:
```
        ent_ab  count_ab  ent_a
0   5197-56744       1.0   5197
1   12766-5197       1.0  12766
2  12766-56744       1.0  12766
3    3091-3162       1.0   3091
4   3091-54583       1.0   3091
```

#### Add column from df_a to df_ab:

`df_ab['ent_a_count'] = df_ab.ent_a.apply(get_ent, args=(df_a, 'ent_a', ))`


#### Add column with `apply`:

```python
def get_ent(ent_df_a, df_a, colname_df_ab):
    row_df_a = df_a[df_a[colname_df_ab] == ent_df_a]
    i = row_df_a.iloc[0]['count']
    return i
```

df_ab
```
        ent_ab  count_ab  ent_a  ent_b  ent_a_count
0   5197-56744       1.0   5197  56744          1.0
1   12766-5197       1.0  12766   5197          2.0
2  12766-56744       1.0  12766  56744          2.0
3    3091-3162       1.0   3091   3162          2.0
4   3091-54583       1.0   3091  54583          2.0
```


### Kendall Tau rank correlation coefficient

```python
def compute_kendall_tau(df_pop):
    # testing
    # x1 = [12, 2, 1, 12, 2]
    # x2 = [1, 4, 7, 1, 0]
    # remove random as they don't have a rank
    df_pop_kendall = df_pop[df_pop.source_tsne == 1]
    x1 = df_pop_kendall['rank_tsne'].values
    x2 = df_pop_kendall['rank_avg_relevance'].values
    tau, p_value = kendalltau(x1, x2) # scipy implementation scipy.stats.kendalltau
    return tau, p_value
```

[read more](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient)