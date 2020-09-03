Title: GloVe
Date: 2017-09-02
Category: GloVe
Slug: GloVe
Summary: Some notes about GloVe Word Embeddings
Status: draft

#### Singular Value Decomposition by Gradient Descent


As an alternative to a full fledged SVD compuation, the matrices $U$ and $V$ can be found using Stochastic Gradient Descent (SGD). This is in many cases preferred because:

 * SVD is slow. 
 * SVD requires care dealing with missing data ([source](https://www.coursera.org/learn/matrix-factorization/lecture/kVjSo/gradient-descent-techniques)).
 * Gradient Descent is much faster and can deal (i.e. ignores) with missing data.
 * In general, Gradient descent is a way to minimize an objective function $J(\Theta)$. [Click here to learn more about SGD](http://cs231n.github.io/optimization-1/).
 
 
 The key idea behind this approach is to find the best k-rank approximation of the original matrix by searching for the matrices with the least error.
 
 * Look at the squared error of individual predictions i.e. the predictions' contribution to the sum of squared errors (SSE).
 
 
 **Simplified SVD**
 
 * Decomposition: $$R = B + PQ^T$$
 
 * Scoring Rule: $$ s(u, i) = b_{ui} + \sum_{f}{p_{uf}q_{if}} $$
 
 * Caveat: This is no longer a true SVD ($P$ and $Q$ are not orthogonal)

<br>

**FunkSVD** (an alternative approach to SGD)
 
 * Train features one at a time
 * Train first feature until convergence
 * Then train the next
 * Ignore missing values (mostly)
 * Learn offset from personalized mean

<br>

**Update Step**
 
 $$\epsilon_{ui} = r_{ui} - s(u,i)$$
 $$\Delta q_{if} = \lambda(\epsilon_{ui}p_{uf} - \gamma q_{if})$$
 $$\Delta p_{uf} = \lambda(\epsilon_{ui}q_{if} - \gamma p_{uf})$$
 
 where $\lambda$ is the learning rate and $\gamma$ is the regularization (biases against extreme value)