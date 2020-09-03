Title: Matplotlib
Date: 2018-01-06
Category: Python
Slug: Matplotlib
Summary: Matplotlib

<br> 

#### Useful Links

* [Plotting with plotnine](https://www.practicaldatascience.org/html/plotting_part2.html)
* [Advanced Histogram Using Python](https://towardsdatascience.com/advanced-histogram-using-python-bceae288e715)
* [A Comprehensive Guide to the Grammar of Graphics for Effective Visualization of Multi-dimensional Data](https://towardsdatascience.com/a-comprehensive-guide-to-the-grammar-of-graphics-for-effective-visualization-of-multi-dimensional-1f92b4ed4149)
* [How to Enhance your Matplotlib Plots](https://towardsdatascience.com/annotating-bar-charts-and-other-matplolib-techniques-cecb54315015)
* [Visualizing statistical plots with Seaborn](https://towardsdatascience.com/visualizing-statistical-plots-with-seaborn-6b6e60ce5e71)
* [DRAWING FROM DATA](https://www.drawingfromdata.com/setting-figure-size-using-seaborn-and-matplotlib)
* [example dynamic label](https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.polynomials.classes.html)


#### Examples

```python
fig, axes = plt.subplots(figsize=(20,10))
sns.set(context="paper", font="monospace")
sns.set_style("white")

plt.title('Title');
ax = (sns.barplot(x=freq_descr.index, y=freq_descr.cnt, color='lightblue'))
_ = ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
```

