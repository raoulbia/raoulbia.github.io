Title: Python Data Structures
Date: 2018-01-03
Category: Python
Slug: python_data_structures
Summary: Python Data Structures

<br>



### Lists

#### itemgetter

itemgetter on a list of tuples `[('P52564', 61), ('O15169', 44), ...]`

`sorted(list(degrees), key=operator.itemgetter(1), reverse=True)[0:5]`

itemgetter on a dict

`sorted(pr.items(), key=operator.itemgetter(1), reverse=True)[0:5]`

#### Compare items in two lists:

```python
for rank_true, rank_pred in zip(true, pred):
    if rank_true == rank_pred:
```

#### Print list items

`print(*myList, sep='\n')`


#### Convert a list of chars into proper list:

```python
list = '123; 456; 887'
ls = list.pop(list).split(';')
```

#### List Comprehension: If/Else

```python
rel_bin = [ None if x == None and y == None
            else x if y == None and not x == None
            else y if x == None and not y == None
            else 0 if x + y == 1
            else 1 if x + y == 2
            else 0 if x + y == 0
            else -9 # to catch any issues
            for x, y in zip(rel_bin_judge_1, rel_bin_judge_2)]
```

<br>

### Dictionaries

#### Counting

```python
context_dic = collections.defaultdict(int)
for res in query_results:
    context_dic[res] += 1
```

#### Count distinct values in a dict key

* `{value: len(list(freq)) for value, freq in groupby(sorted(schedule_rel_types))}`

#### Count unique values using `Counter` class

```python
d = Counter(self.co_occurrence_counts['Gene_Gene']['ent_ab'])
    for k, v in d.most_common(5):
        print('%s: %i' % (k, v))
```

see also [dictionary count of unique values](https://stackoverflow.com/questions/16406329/python-dictionary-count-of-unique-values)

<br>

### Named Tuples

```python
print(self.results[0]._fields)
print(', '.join(['{0}={1}\n'.format(k, getattr(self.results[0], k)) for k in self.results[0]._fields]))

self.Result = collections.namedtuple('Result', ('embedding', 'entity', 'type',
                                                       'precision', 'recall',...))
self.results = []
elf.results.append(self.Result(embedding=source,
                                          entity=entity,
                                          type=type,
                                          precision=precision,
                                          recall=recall,
                                          ...
                                          ))
results_df = pd.DataFrame(results, columns=results[0]._fields)
t_by_emb = results_df.groupby(['embedding']).mean()
t_by_emb_bio = results_df.groupby(['embedding', 'entity']).mean()
t_by_emb_type = results_df.groupby(['embedding', 'type']).mean()
t_by_emb, t_by_emb_bio, t_by_emb_type = t_by_emb.T, t_by_emb_bio.T, t_by_emb_type.T
```

**Note**: Named tuples are immutable, so you cannot manipulate them. If you want something mutable, you can use recordtype.
[read more](https://stackoverflow.com/questions/31252939/changing-values-of-a-list-of-namedtuples)


<br>

