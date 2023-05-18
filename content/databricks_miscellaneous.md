Title: Databricks Misc.
Date: 2023-01-24
Category: Databricks
Slug: databricks_miscellaneous
Summary: Databricks Misc.


#### Code Snippets
```
SELECT * FROM _v_objects where objtype = 'TABLE' and objname like '%PCM%'
SHOW COLUMNS IN team_data.dds_perf_guar_by_week
DESCRIBE TABLE EXTENDED ORX_IDW_DM_OFSH_INTR_VIEW_PRD.V_D_MEMBER_ADJUD
DESCRIBE DETAIL ORX_IDW_DM_OFSH_INTR_VIEW_PRD.V_D_MEMBER_ADJUD (only for tables, NOT views)
DESCRIBE HISTORY table_name
```
```
today = datetime.today().strftime('%Y-%m-%d')
today_nodash = today.replace('-','')
today_slash = datetime.today().strftime('%d/%m/%Y')
fpath = f"/mnt/userspace/custom_dataset/.../INPUT_FILES/fda_drugshortages_{today}.xlsx"
```

#### Import Notebook
```
%run "../../schemas/master_config"
```

#### Filter Dataframe Rows by Column Values
```
df = df.filter( (df.COL_A == i) & (df.COL_B.isin(['R','S'])) )
```

#### Databricks CLI

* `pip install databricks-cli`
* `export PATH="$HOME/.local/bin:$PATH"`
* `/home/username/.local/bin/databricks configure`
* List existing secret scopes: `databricks secrets list-scopes`


