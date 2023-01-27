Title: Databricks Misc.
Date: 2023-01-24
Category: Databricks
Slug: databricks_miscellaneous
Summary: Databricks Misc.


a#### Import another notebook
```
%run "../../schemas/master_config"
```

#### Fitler DataFrame rows by Column values
```
df = df.filter( (df.COL_A == i) & (df.COL_B.isin(['R','S'])) )
```

#### Databricks CLI

* `pip install databricks-cli`
* `export PATH="$HOME/.local/bin:$PATH"`
* `/home/username/.local/bin/databricks configure`
* List existing secret scopes: `databricks secrets list-scopes`


