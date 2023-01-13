Title: Databricks Misc.
Date: 2023-01-24
Category: Databricks
Slug: databricks_miscellaneous
Summary: Databricks Misc.


#### Import another notebook
```
%run "../../schemas/master_config"
```

#### Fitler DatFrame rows by Column values
```
df = df.filter( (df.COL_A == i) & (df.COL_B.isin(['R','S'])) )
```

