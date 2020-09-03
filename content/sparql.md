Title: SPARQL
Date: 2017-08-05
Category: SPARQL
Slug: SPARQL
Summary: SPARQL

A collection of [SPARQL queries](https://en.wikipedia.org/wiki/SPARQL) I found useful.

Note that the queries are use case-specific but they should be easy to generalize. Do ignore the fact that lines are
commented out. In the original setting I used this approach to quickly select the one or other query.


    from SPARQLWrapper import SPARQLWrapper, JSON
    sparql = SPARQLWrapper("http://localhost:3030/angioexplain3/query")
    sparql.setQuery("""

                        ### Check for reflexive triples in the quads ############################

                        # SELECT (count (?s) as ?nb)
                        # {
                        #  GRAPH ?g {?s ?p ?s}
                        # }


                        ##### COUNT QUADS / TRIPLES BY RELATION #################################

                        # --- ANY INTERACTION ----------------------------------

                        # SELECT ?res (COUNT (?res) as ?cnt)
                        # {
                        #     {GRAPH ?g {?s ?res ?o} }
                        #     UNION
                        #     {?s ?res ?o}
                        # }
                        # GROUP BY ?res ORDER BY DESC (?cnt)  #LIMIT 10


                        # --- WITH SPECIFIC INTERACTION e.g. protein to protein --------

                        # SELECT ?res (COUNT (?res) as ?cnt)
                        # {
                        #     {
                        #     {GRAPH ?g {?s ?res ?o} FILTER regex( str(?s), "protein") }
                        #     {GRAPH ?g {?s ?res ?o} FILTER regex( str(?o), "protein") }
                        #     }
                        #     UNION
                        #     {
                        #     {?s ?res ?o FILTER regex(str(?s), "protein")}
                        #     {?s ?res ?o FILTER regex(str(?o), "protein")}
                        #     }
                        # }
                        # GROUP BY ?res ORDER BY DESC (?cnt) LIMIT 10

                        # # --- WITH PROTEIN 2 PROTEIN COUNT ONLY --------
                        #
                        # SELECT COUNT (?res)  # DOENS'T WORK ON GOZILLA !??
                        # {
                        #     {
                        #     {GRAPH ?g {?s ?res ?o} FILTER regex( str(?s), "protein") }
                        #     {GRAPH ?g {?s ?res ?o} FILTER regex( str(?o), "protein") }
                        #     }
                        #     UNION
                        #     {
                        #     {?s ?res ?o FILTER regex(str(?s), "protein")}
                        #     {?s ?res ?o FILTER regex(str(?o), "protein")}
                        #     }
                        # } LIMIT 10


                        ######## QUERYING GRAPHS / QUADS ##################################

                        ## Example 1: COUNT UNIQUE PATHWAYS
                        # Note: pathways are stored as graphs in quads

                        # SELECT (COUNT (DISTINCT ?res) as ?cnt)
                        # {
                        #     {GRAPH ?res {?s ?p ?o} FILTER regex( str(?res), "/Pathway" ).}
                        # }
                        # ORDER BY DESC (?cnt)


                        ##### PUBTATOR  ###################################################

                        #-------- COUNT UNIQUE PUBMEDID's ------------------------------

                        # From Quads
                        # SELECT COUNT (DISTINCT ?res)
                        # {
                        #     GRAPH ?res {?s ?p ?o} FILTER (strstarts( str(?res), "http://identifiers.org/pubtator/" )).
                        # }

                        # From Title triples
                        # SELECT COUNT (DISTINCT ?res)
                        # {
                        #     ?res ?p ?o FILTER (strstarts( str(?res), "http://identifiers.org/pubtator/" )).
                        # }


                        #--------- PUBTATOR COUNT RELATIONS e.g. Gene_Disease----------------

                        # SELECT ?res (COUNT (?res) as ?cnt)
                        # {
                        #     {GRAPH ?g {?s ?res ?o} FILTER ( regex( str(?g), "pubtator/pubmedid") ) }
                        #
                        #     # MINUS
                        #     # {GRAPH ?g {?s ?res ?o} FILTER ( regex( str(?s), "species") ) }
                        #     # MINUS
                        #     # {GRAPH ?g {?s ?res ?o} FILTER ( regex( str(?o), "species") ) }
                        #
                        # }
                        # GROUP BY ?res ORDER BY DESC (?cnt)


                        #--------- PUBTATOR SPECIES -----------------------------------------

                        # Get count of abstracts by species ID

                        # SELECT COUNT (DISTINCT (?g))
                        # {
                        #     {GRAPH ?g {?s ?p ?o} FILTER regex( str(?p), "Species") }
                        # }
                        # GROUP BY ?g ORDER BY DESC (?cnt) LIMIT 5


                        # Get the number of documents without species or with at least mention of human if any specified
                        # Pierre-Yves

                         # SELECT (COUNT( DISTINCT ?g) AS ?nbPubmedDocuments)
                         # {
                         #    # get only pubtator named graph
                         #    GRAPH ?g
                         #    {
                         #        ?s ?p ?o
                         #        FILTER ( strstarts(str(?p), "http://identifiers.org/pubtator/"))
                         #        FILTER ( !strstarts(str(?o), "http://identifiers.org/species/")) .
                         #
                         #    }
                            #
                            # MINUS
                            #
                            # {
                            #     # get quads with species
                            #     SELECT ?g
                            #     {
                            #         {
                            #             GRAPH ?g
                            #             {
                            #                  ?s ?p ?o
                            #                  FILTER ( strstarts(str(?s), "http://identifiers.org/species/")) .
                            #             }
                            #         }
                            #         UNION
                            #         {
                            #             GRAPH ?g
                            #             {
                            #                  ?s ?p ?o
                            #                  FILTER ( strstarts(str(?o), "http://identifiers.org/species/")) .
                            #             }
                            #         }
                            #     }
                            # }
                         # }





                        ##### ENTITIES #####################################################

                        # --- COUNT ENTITIES e.g Entrez#123 (gene), ... -----------------

                        # SELECT ?res (COUNT (?res) as ?cnt)
                        # {
                        #     {GRAPH ?g {?res ?p ?o} FILTER regex( str(?res), "/gene/" )}
                        #     UNION
                        #     {GRAPH ?g {?s ?p ?res} FILTER regex( str(?res), "/gene/" )}
                        #     UNION
                        #     {?res ?p ?o FILTER regex(str(?res), "/gene/")}
                        #     UNION
                        #     {?s ?p ?res FILTER regex(str(?res), "/gene/")}
                        # }
                        # GROUP BY ?res ORDER BY DESC (?cnt) LIMIT 10


                        # --- COUNT ENTITY TYPE e.g. Gene, Drug --------------------------

                        # SELECT COUNT (DISTINCT ?res)
                        # {
                        #     {GRAPH ?g {?res ?p ?o} FILTER regex( str(?res), "/gene/" )}
                        #     UNION
                        #     {GRAPH ?g {?s ?p ?res} FILTER regex( str(?res), "/gene/" )}
                        #     UNION
                        #     {?res ?p ?o FILTER regex(str(?res), "/gene/")}
                        #     UNION
                        #     {?s ?p ?res FILTER regex(str(?res), "/gene/")}
                        # }

                        # SELECT COUNT (DISTINCT ?res)
                        # {
                        #     {?res ?p ?o FILTER regex(str(?res), "/disease/")}
                        #     UNION
                        #     {?s ?p ?res FILTER regex(str(?res), "/disease/")}
                        # }

                        # --- QUADS COUNT ENTITY TYPE e.g. Pathways --------------------------

                        # QUADS
                        # SELECT COUNT (DISTINCT ?res)
                        # {
                        #     {GRAPH ?res {?s ?p ?o} FILTER regex( str(?res), "/Pathway_" )}
                        #     # UNION
                        #     # {GRAPH ?res {?s ?p ?o} FILTER regex( str(?res), "/Pathway_" )}
                        # }

                        # QUADS
                        # SELECT ?res (COUNT (?res) as ?cnt)
                        # {
                        #     {GRAPH ?g {?s ?res ?o} FILTER ( regex( str(?g), "/Pathway_") ) }
                        # }
                        # GROUP BY ?res ORDER BY DESC (?cnt)

                        # QUADS
                        # SELECT COUNT ( ?res)
                        # {
                        #     {GRAPH ?g {?s ?res ?o} FILTER regex( str(?res), "/ppi/" )}
                        # }


                        """)




    sparql.setReturnFormat(JSON)
    results = sparql.query().convert() # is a Dict.

    # print(results)
    # print(len(results["results"]["bindings"]))
    # print(len(results), results)
    # print(results["head"].values())

    # establish the type of out pput we get from the query e.g. ['res', 'cnt']
    # this is used to shape the if/else statements below
    vars = []
    for listOfVars in results["head"].values():
        for var in listOfVars:
            vars.append(var)
    print(vars)

    try:
        if len(vars) > 1:
                for result in results["results"]["bindings"]:
                    print("\t".join([result[var]["value"] for var in vars]))
        elif vars == [".1"]:
                for result in results["results"]["bindings"]:
                    print(result[var]["value"])
        else:
            try:
                # print results without prefix
                for result in results["results"]["bindings"]:
                    print(result[var]["value"].split("#")[1])
            except:
                # print simple count
                for result in results["results"]["bindings"]:
                    print(result[var]["value"])
    except:
        print("no data found for query")
