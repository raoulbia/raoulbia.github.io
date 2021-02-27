Title: RMD
Date: 2018-02-20
Modified: 2010-12-05 19:30
Category: RMD
Slug: rmd
Summary: RMD

#### Useful Snippets

* Footnote: `...some text.^[footnote]`

#### Exploring Factor Combinations: Dual Boxplots

```
plot <- ggplot(df, aes(x=SBA_Portion.groups:New, y=GrAppv)) + 
  geom_boxplot(lwd=0.1, outlier.size = 0.1) + 
  labs(x = "SBA Guaranteed Portion : New Business") +
  theme(plot.title = element_text(size=10),
        # axis.ticks.y = element_blank(),
        # axis.text.y = element_blank(),
        axis.title.x = element_text(size=8),
        axis.title.y = element_text(size=8)) + 
  geom_vline(xintercept = 2.5, linetype="dashed", size=0.2) +
  geom_vline(xintercept = 4.5, linetype="dashed", size=0.2)

ggrob <- ggplotGrob(plot)
grid.arrange(ggrob, ncol=1)
```
#### Histogram w/Optimum Bin Width

```
binw <- 2 * ( IQR(statistic) / length(statistic)^(1/3) ) 

ggplot(data.frame(statistic), aes(statistic)) + 
  geom_histogram(aes(y=..density..),
                 binwidth = binw,
                 fill="darkred",
                 colour="black",
                 size=1) + 
  geom_density(aes(y=..density..),
               size=1) + 
  labs(x= "Mean", y= "Density", 
       title = "Distribution of sample means")
```

#### Related Links

* [ggplot2 examples](https://rpubs.com/raoulbia/slr)
* [SO: Rotating Axis labels](https://stackoverflow.com/questions/1828742/rotating-axis-labels-in-r)
* [How to calculate number of bins for a histogram](https://www.xspdf.com/resolution/52805925.html)

#### R: Other Links

* [Notebooks with R Markdown](https://channel9.msdn.com/Events/useR-international-R-User-conference/useR2016/Notebooks-with-R-Markdown)
