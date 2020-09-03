Title: Pandas
Date: 2018-01-28
Category: Python
Slug: pandas
Summary: Python Data Analysis Library


#### Useful Links

* [Sidetable - Create Summary Tables](https://pbpython.com/sidetable.html)
* [Sidetable Gives You the Pandas Methods You Didn't Know You Needed](https://deepnote.com/article/sidetable-pandas-methods-you-didnt-know-you-needed)
* [crosstabs() Method: Compute Aggregated Metrics Across Categorical Columns](https://dfrieds.com/data-analysis/crosstabs-python-pandas.html)
* [7 Simple Python Functions to Clean Your Data](https://towardsdatascience.com/automate-boring-tasks-with-your-own-functions-a32785437179)


### Imports

```python
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport 

import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
```

### IO

#### Read CSV

```python
fp = '../local-data/data.csv'
df = pd.read_csv(fp,
                 dtype=str,
                 encoding='ISO-8859-1', # to prevent unicode error
                 keep_default_na=True,
                 dayfirst=True,
                 parse_dates = date_cols)
df.shape
```

#### Read XLS

```python
df = pd.read_excel("../local-data/file.xlsx", 
                  dtype=str,
                  encoding = "ISO-8859-1",
  				  skiprows=[0,1], 
				  header=0,
				  skip_footer=0, 
				  index_col=None, 
				  names=None, 
				  sheet_name=0))
```

#### Read tsv.gz

```python
from bz2 import BZ2File as bzopen

df = pd.read_csv('STRING_triples.tsv.gz', nrows=100, compression='gzip',
           error_bad_lines=False, delimiter='\t')

with bzopen("STRING_context-restricted.tsv.bz2", "r") as bzfin:
lines = []
for i, line in enumerate(bzfin):
    # if i == 10000: break
    lines.append(line.rstrip())
```

#### Read Multiple Files in Directory
```
import glob
li = [] # add dataframes to this list
path = '../local-data/original/new'
all_files = glob.glob(path + "/*")
for filename in all_files:
    print(filename)
    tmp = pd.read_excel(filename, 
                  dtype=str,
                  encoding = "ISO-8859-1")
    print(tmp.shape)
    li.append(tmp)
    del tmp
    
# make a dataframe of all the files combined
df = pd.concat(li, axis=0, ignore_index=True)
df.shape
```
    
#### Write

`df.to_csv("../local-data/output/shuba_data_subset.csv", index=True)`

### Handling Dates

#### Create Date Features
```
# time conversion helper variables
seconds_in_day = 60 * 60 * 24
seconds_in_hour = 60 * 60

# Create new feature: Resolution Time
data['resolution_time_secs'] = data.resolved_at - data.opened_at

# convert to seconds
data['resolution_time_secs'] = (data['resolution_time_secs']
                                .apply(lambda x : x.total_seconds()))

# convert resolution time to days
data['resolution_time_days'] = data['resolution_time_secs'].copy()
data['resolution_time_days'] = (data['resolution_time_days']
                                .apply(lambda x : x // seconds_in_day + 1))

# convert resolution time to hours
data['resolution_time_hrs'] = data['resolution_time_secs'].copy()
data['resolution_time_hrs']= (data['resolution_time_hrs']
                              .apply(lambda x : x // seconds_in_hour))
                              
```

#### Select by Year
```
# data = data[data.opened_at.dt.year >= 2019]
```

### Inspect

#### Duplicate rows

`print('# of duplicate rows:{}'.format(len(df)-len(df.drop_duplicates())))`

#### Duplicates in a column

`df.duplicated(subset='col_name', keep='first').count()`

#### Count missing values

```python
missing = df.copy().isna().sum()
(missing.reset_index(name='cnt')
 .sort_values(by='cnt', ascending=True))
```

or

```python
num_avg_rel_isnan = df['avg_relevance'].notnull().sum()`
```

### Drop 

#### Drop rows if index is NA

`df = df[df.index.notna()]`

#### Drop rows if value in a specific column is NA

`df = df[df.col_name.notna()]`


### Consolidate Column Levels

#### to prevent `SettingWithCopyWarning `

```python
kw = ['Email', 'Phone', 'Self-service']
df = (df.assign(**{'category2': np.where(df.category.isin(kw), 
                                         df.category, 
                                         'Other')}))
```

#### with `apply`

```python
kw = ['Email', 'Phone', 'Self-service']
df['contact_type2'] = (df.contact_type.apply(lambda x : x
                                              if any([k in x for k in kw])
                                              else 'Other'))
df.contact_type2.value_counts(normalize=True)
```


### Replace values

#### Replacing values in a column

`df['female'] = df['female'].replace({'female': 1, 'male': 0})`

#### Replace NA with 'Other'

```python
df = df.copy()
print(df['category'].isna().sum())
df.loc[:, 'category'].fillna('Other', inplace=True)
print(df['category'].isna().sum())
```

##### Replace empty string with NA then drop NA's

```python
df.replace(r'^\s*$', np.nan, regex=True) 
df.dropna()
```

#### Replace True/False by 1/0

use `astype(int)` to convert values to 0 and 1

`df['new_col'] = df['B'].isin([3, 2]).astype(int)`


### Create New Feature

#### Create a boolean feature column

```
data['is_WE'] = (data.opened_at.apply(lambda x : 1 
                                      if x.strftime('%A') in['Saturday', 'Sunday']
                                      else 0)).astype('category')
```

or...using shizen-gengo text search

```
data['is_costa'] = 0
costa_inc_nbrs = explore_utils.search(data, 'description', 'costa').reset_index().number
data.loc[costa_inc_nbrs.tolist(), 'is_costa'] = 1
len(data[data.is_costa==1])
```                                     

#### Add column with new value based on values in other cols:

```
conditions = [
    (data.company == 'unknown') &  (data.is_costa == 1)
]
outputs = ['costa']
data.company = np.select(conditions, outputs, data.company)
```

### Merge

#### Merge on index

```python
df = (df1.merge(df2,
                how='left',
                suffixes = ['_x', '_y'],
                left_index=True, 
                right_index=True))
print(df.shape)
```

### groupby

#### generic groupby

```

```

```python
(df.groupby('caller')
 .size()
 .to_frame()
 .reset_index()
 .rename(columns={0:'cnt'})
 .sort_values(by='cnt', ascending=False)
).head()
```

#### groupby with dates

```
tmp.groupby(tmp['opened_at'])['number']
         .size()
         .reset_index(name='cnt')
         .sort_values(by=['opened_at', 'cnt'], ascending=[True, False]
```

#### Adding counts from a groupby(): mapping with a dict

```python
gpd = df.groupby...
d = dict(zip(gpd.caller, gpd.cnt))
df['nbr_tickets_opened'] = df.customer_display_name.map(d)
df.head()
```

### Selecting Data

#### List of column names to select

```
cols = ['colname1', 'colname2]
df = df2.loc[:, cols]
```

#### Conditional search

```python
self.df_co_occurrences[
    (self.df_co_occurrences.ent_a == '4040')
        (self.df_co_occurrences.ent_b == '5267')]
```

#### Get two columns for a specific row

`embeddings_df.ix[[input_entity_uri]][['transformed_x', 'transformed_y']]`

#### Find rows by column index and with condition

`assign_clusters_df[assign_clusters_df[1]==2]`

#### Select with `iloc` or `loc`

iloc

`if embeddings_df.iloc[row_id].name == input_entity_uri`

loc

```python
def get_pmi(ent_ab, df, count_ab, ent_a_count, ent_b_count):
    count_ab = df.loc[df['ent_ab'] == ent_ab, 'count_ab'].iloc[0]
    ent_a_count = df.loc[df['ent_ab'] == ent_ab, 'ent_a_count'].iloc[0]
    ent_b_count = df.loc[df['ent_ab'] == ent_ab, 'ent_b_count'].iloc[0]
    return count_ab / (ent_a_count * ent_b_count)	
```

#### Select based on regexp: `str.contains()`

```python
import re
tmp = tmp[tmp.description.str.contains("(?i)gps")]
```

#### Select based on Frequency threshold

```python
freq_cat = dat['category'].value_counts(normalize=True) * 100
freq_cat = freq_cat.reset_index(name='pct').set_index('index').rename_axis(None)
t = 0.2
freq_cat = freq_cat[freq_cat.pct>=t]
```


### Drop / Remove Data

#### Remove elements from a lookup list

`df = df[~df.uri.isin(list_cluster_entities)]`

#### Drop any NaN in any column

`embeddings_bio_df = embeddings_df[~embeddings_df.isin(['NaN']).any(axis=1)]`

#### Drop a spcific column

`neighbors_df = neighbors_df.drop('uri.1', 1)`


### Sorting

#### Sort a column by the values in another

```python
df_typed['rank_avg_relevance'] =
    df_typed.groupby('source_tsne')['avg_relevance'].rank(ascending=False)
```
or

`mentionList = sorted(tuple(mentionList), key=lambda x: x[1])`

source: [How to sort multidimensional array by column?](http://stackoverflow.com/questions/20183069/how-to-sort-multidimensional-array-by-column)


###  Concatenate rows from multiple files into one DF

```python
def read(input_eval_dp):
    files = os.listdir(input_eval_dp)

    # add all scores from the various files to one DF
    eval_df = pd.DataFrame()
    for file in files:
        print(files)
        fp = os.path.join(input_eval_dp, file)
        print(fp)

        tmp_df = get_eval(fp)
        eval_df = pd.concat([eval_df, tmp_df])
        # print(eval_df.shape)
    # print(eval_df.head())
    return eval_df
```

### Zero Variance: Exclude columns with only one level

```python
criteria = pd.DataFrame(df_final.describe().transpose()['unique']>1)
criteria = criteria.iloc[:,0]
df_final = df_final[df_final.columns[criteria]]
df_final.shape
```

or

```python
nunique = data.apply(pd.Series.nunique)
cols_to_drop = nunique[nunique == 1].index
data = data.drop(cols_to_drop, axis=1)
data.shape
```

or, based on standard deviation

```python
cols = data.select_dtypes([np.number]).columns
std = data[cols].std()
cols_to_drop = std[std==0].index
data = data.drop(cols_to_drop, axis=1)
```

### Misc.

#### Create sample dataset
```
tmp = df.sample(10000)
tmp.to_csv("../local-data/output/bat_sample2_original_headers.csv", index=False)
del tmp
```

#### np.where()

```python
df['is_fujitsu_owned'] = np.where(df['resolvergroup1']=='Fujitsu', True, False)
df['is_fujitsu_owned'].value_counts(normalize=True)
```

#### Get quick proportions

`df['is_pw_reset'].value_counts(normalize=True)`

#### Prevent line break when printing list

`print(sorted( set(dat.category.unique()) ), end='')`

#### Convert to Categorical dtype

`df['contact_type'] = df['contact_type'].astype("category")`

#### Dataframe to List

Convert dataframe column to list

`entity_list = entity_list_df['uri'].tolist()`

Create one big list of ID's from two DF columns that contain IDs

```python
triples = pandas.read_csv(f, sep='\t').ix[:, [0, 2]].as_matrix()
phosphonetowrk_IDs = set(triples.flatten())
```
#### Working with Tuples

```python
phrases_df = phrases_df.fillna('(a,a)')
for col in phrases_df.columns:
    phrases_df[col]  = phrases_df[col].str[1]
phrases_df.head()
```

or

```python
phrases = phrases.fillna('(,)')
for col in phrases.columns:
    phrases[col] = phrases[col].apply(lambda x:x.split(",")[1]
                         .replace(" '", "")
                         .replace("'", "")
                         .replace(")", ""))
phrases.head()
```

#### Crosstab

```python
df = dat.copy()
df = df[df.country.isin(['Russian Federation'])]
tmp = pd.crosstab(df.bat_5tc_service.astype(str), # ROWS
                  df.country,                     # COLS
                  values=df.incident_id, 
                  aggfunc=pd.Series.nunique,
                  margins=True,
                  dropna=False)#.fillna(value=0)
tmp.sort_values(by='All', ascending=False).head()
```

### Links to review

* [A Really Simple Way to Edit Row by Row in a Pandas DataFrame](https://towardsdatascience.com/a-really-simple-way-to-edit-row-by-row-in-a-pandas-dataframe-75d339cbd313)