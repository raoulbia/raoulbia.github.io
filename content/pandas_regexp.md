Title: Pandas Regular Expressions
Date: 2018-01-27
Category: Python
Slug: pandas_regexp

#### Extract Substring

```
# obtain Title from name (Mr, Mrs, Miss etc) by extracting up to but excluding the first dot (.)
df['Title'] = df.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
```

#### String Matching

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

