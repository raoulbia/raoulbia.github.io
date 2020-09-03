Title: RDFLib Graph Object
Date: 2017-08-04
Category: Python
Slug: python, rdflib
Summary: RDFLib (Python) Code Snippets

On this page I keep snippets of code I have found useful when working with the
[RDFLib library](https://rdflib.readthedocs.io/en/stable/). Specifically, the code snippets show how to

* load a triple (.n3) or quad (.nq) file RDFLib graph object
* read from an RDFLib graph object


##### Loading a triple/quad file into an RDFLib object


```python
g = rdflib.ConjunctiveGraph()
for file in os.listdir(input_kg_dir_path):
    if file.endswith(tuple(f_extension)):
        filepath = os.path.join(input_kg_dir_path, file)
        # read each kg file and build a graph
        print('reading {}'.format(filepath))
        try:
            g.parse(filepath, format=rdflib.util.guess_format(filepath))
        except Exception as e:
            print(e)
return g
```

##### Reading an RDFLib graph object


```python
for entity in entity_list:
    print(entity_list)
    query_results = angio_kg.query( # is an rdflib conjunctive raph object which has a parse method
        """SELECT DISTINCT ?g
        {GRAPH ?g {
              {<%s> ?p ?o}
              UNION {?s ?p <%s>}
         }}""" % (entity, entity))
```