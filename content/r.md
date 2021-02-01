Title: R
Date: 2018-02-20
Modified: 2010-12-04 19:30
Category: R
Slug: R
Summary: R

#### Useful Snippets

* Filter: ```df %>% filter(., GrLivArea >=4000 & SalePrice < 200000)```
* Remove observations: ```df <- df[-c(524, 1299), ]```
* Reomve column: ```df$colname<- NULL```
* Order columns alphabetically: ```df <- df[ ,order(colnames(df))]```
* Convert: ```df$colname <- as.integer(df$colname)```
* Make df with only numeric vars: ```num_df <- df[, sapply(df, is.numeric)]```
* Correlation: ```cor(num_df, use="complete.obs")```
* random sampling from each factor: ```olive_sample <- ddply(olive,.(region),function(x) x[sample(nrow(x),10),])```
* to access the 1rst and 3rd elements of a vector: ```my.vec[c(1,3)]```

#### Creating vectors and matrices

* ```my.vec <- c(1:4)```
* ```my.vec <- c(TRUE, FALSE, FALSE, FALSE, TRUE, TRUE)```
* ```A <- matrix(c(1,2,2,5), nrow=2, ncol=2, byrow=TRUE)```

#### Script Header

```
library(rstudioapi)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
rm(list=ls())

library(rio) # import csv
```

#### Read Data

`load("data_project_backpain.RData")`

```
data  <- import('superstore.csv', setclass = "tibble")
head(data)
```
#### Select only numeric columns

```
nums <- unlist(lapply(df, is.numeric))  
df[ , nums]
```

#### Coerce multiple columns to factors at once

```
cols <- c("A", "C", "D", "H")
df[cols] <- lapply(df[cols], factor)  ## as.factor() could also be used
```

#### Exclude columns by name

```
exclude <- c("Neighborhood", "Exterior2nd",)
df[ , -which(names(df) %in% exclude)]
```

#### Count Missing Values

`sapply(df, function(x) sum(is.na(x)))`

#### Create vector from column and drop missing values

```
x <- gt[!is.na(gt$LandAverageTemperature), 2]
```

#### Making Objects available to RMarkdown

* in R script

`save(all = TRUE, file= "all.rda")`
`save(object1.name, object2.name, file= "all.rda")`


* in RMD file

`load("all.rda")`


#### Benchmarking

```
libray(microbenchmark)
microbenchmark(
  bad_cpp = bad_select_positive_values_cpp(x),
  good_cpp = good_select_positive_values_cpp(x),
  times = 1
)

library(rbenchmark)
benchmark(
  bad_select_positive_values_cpp(x),
  good_select_positive_values_cpp(x),
  order = "relative"
)
```

#### Profiling

```
Rprof("profile1.out" ) #send profiling to profile1.out
# <call function here>
Rprof(NULL)
summaryRprof("profile1.out")
```

#### Sliding Window

How sliding window works:

* select subset of x of size 3 using its indices
* 1st iter: x[3 - 3 + 1, 3] gives x[1, 3]
* 2nd iter: x[4 - 3 + 1, 4] gives x[2, 4]
* ...

```
window <- 3 
for(i in seq(window, n)) {
x_subset <- x[seq(i - window + 1, i)]
res[i] <- mean(x_subset)
}
```

#### R: Packages

* [caret](https://heartbeat.fritz.ai/using-caret-in-r-to-classify-term-deposit-subscriptions-for-a-bank-bd40ff5cc15)
* [Using the recipes package for easy pre-processing](http://www.rebeccabarter.com/blog/2019-06-06_pre_processing/)
* [bestNormalize](https://cran.r-project.org/web/packages/bestNormalize/vignettes/bestNormalize.html)

#### Related Links

* [Populating Missing Dates with Complete and Fill Functions in R and Exploratory](https://blog.exploratory.io/populating-missing-dates-with-complete-and-fill-functions-in-r-and-exploratory-79f2a321e6b5)
* [MarinStatsLectures](https://www.youtube.com/user/marinstatlectures/playlists)
* [Data Cleaning with R and the Tidyverse: Detecting Missing Values](https://towardsdatascience.com/data-cleaning-with-r-and-the-tidyverse-detecting-missing-values-ea23c519bc62)
* [Play With Your ML Dataset - Cheatsheet in R](https://medium.com/x8-the-ai-community/play-with-your-ml-dataset-cheatsheet-in-r-bd8451ec6dd7)
* [Coding in R: Pivot Painlessly](https://towardsdatascience.com/coding-in-r-pivot-painlessly-32e40a0b6c3d)
* [Simple Fast Exploratory Data Analysis in R with DataExplorer Package](https://towardsdatascience.com/simple-fast-exploratory-data-analysis-in-r-with-dataexplorer-package-e055348d9619)
* [Wrap column name in pdf table, from knitr::kable](https://community.rstudio.com/t/wrap-column-name-in-pdf-table-from-knitr-kable/3278)
* [A Guide to Machine Learning in R for Beginners: Logistic Regression](https://medium.com/analytics-vidhya/a-guide-to-machine-learning-in-r-for-beginners-part-5-4c00f2366b90)
* [Clean Up Your R Code! A Secret to Better Feature Engineering](https://towardsdatascience.com/tired-of-nested-ifelse-in-dplyr-look-no-further-ebf7166b5289)
* [Group Manipulation In R](https://medium.com/analytics-vidhya/group-manipulation-in-r-3-5554a0c1b544)
* [The Best Resources for R Programming](https://medium.com/@moorissa/the-best-resources-for-r-programming-37dbc94e0de6)
