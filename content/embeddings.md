Title: Embeddings
Date: 2017-09-01
Category: Embeddings
Slug: embeddings
Summary: Some notes about Embeddings

On this page I keep some notes abbout [GloVe]({filename}./embeddings_glove.md)
and word2vec word embeddings. 

#### various notes

* Word embeddings are based on the **distributional hypothesis**:

      A word’s meaning is encoded in the 
      frequencies with which other words 
      occur near it in natural text.
    
  In other words, a word’s environment encodes a great deal of semantic information. 
  For example, we can infer that *oculist* and *eye-doctor* are synonyms from the fact that they are found 
  near the same words in a given corpus.  

* Algorithms like singular value decomposition (SVD) or principle components analysis (PCA)
  can be used to compress an `n × m` feature matrix M to an `n × k` matrix M' (where k << m) 
  in such a way that M' retains most of the information of M. 
      
  [source](https://universalflowuniversity.com/Books/Computer%20Programming/Data%20Mining%20and%20Data%20Science/The%20Data%20Science%20Design%20Manual.pdf)
      
* Word representations can be obtained using 

  * co-occurrence counts (derived directly from corpus counts
  * using association measures such as Point-wise Mutual Information (PMI)
  * lower-rank representations such as PPMI-SVD and GloVe ([source](https://arxiv.org/pdf/1606.00819.pdf)) 
  * predictive methods e.g. skip-gram (word2vec)

* A co-occurrence matrix by itself provides word vectors which can in principle be used to compute 
  similarities between words. These vectors are how ever high-dimensional and sparse. 

* There are two approaches to converting high-dimensional and sparse word vectors to low-dimensional and 
  dense vectors:
  
  * dimensionality reduction e.g. SVD
  * direct learning e.g. word2vec, GloVe

* For each unique word, word embedding methods aim to find a vector that summarizes its environment 
  and hence reveals its semantics. 

* Algebraic relationships between word vectors correspond to semantic relationships between words.  
  For example, it is typical to find that 
  
  `f(France) ≈ f(England) + f(Paris) − f(London)`
   
  i.e. “France is to England as Paris is to London”. 
  ([source](https://uwaterloo.ca/scholar/sites/ca.scholar/files/pa2forsy/files/project_dec_3.pdf)) 

* You can check how good a word embedding is by finding the top 10 nearest neighbors of a word.

#### word2vec

* word2vec consist of two functions:

  * *f*, which maps words to a word vector
  * *g*, which, given a word’s vector, produces an estimate of the probability of finding each other 
    word in vocabulary $V$ near that word in the corpus.
   
   where 
   * the values of a given word vector are the parameters we determine when learning g.
   * *f* and *g* are trained by stochastic gradient descent so that each predicted word is probable, given
     its predictor word
   
      
#### GloVe 

* GloVe produces embeddings by factorizing the logarithm of the corpus word co-occurrence matrix.

* *We tokenize and lowercase each corpus with the Stanford tokenizer, build a vocabulary of the 400,000 most frequent 
 words, and then construct a matrix of co-occurence counts… we use a decreasing weighting function so that word pairs 
 that are d words apart contribute 1/d to the total count.*
 

* `#TODO` look up 1st order vs. 2nd order co-occurrences > see Coursera video

* While this produces embeddings which are similar to [word2vec](https://code.google.com/p/word2vec/)
(which has a great python implementation in [gensim](http://radimrehurek.com/gensim/models/word2vec.html)), 
the method is different!

* co-occurrence: underlying assumption that the meaning of each word can be captured through its co-occurrence pattern 
with context words


#### Glossary

* skip-bigram: count how many times a pair of words occurs together in sentences irrespective of their 
  positions in sentences.

* Word vector dimension: Actually the word vector dimension does not reflect the vocabulary size. 
  What Word2Vec is doing is mapping the words to their representation in a vector space and you can 
  make this space of any dimension you want. 
  [source](https://stackoverflow.com/questions/38137551/what-is-word-vector-dimension)


#### Resources


**Resources covering both word2vec and Glove**

* [Applied Deep Learning](https://www.csie.ntu.edu.tw/~yvchen/f105-adl/doc/161013_WordVector2.pdf)(slides)
* [Word vectors and the distributional hypothesis](https://uwaterloo.ca/scholar/sites/ca.scholar/files/pa2forsy/files/project_dec_3.pdf)
(focus is on word2vec; good description of the underlying theory)
* [Matrix Factorization using Window Sampling and Negative Sampling for Improved Word Representations](https://arxiv.org/pdf/1606.00819.pdf)
* [Word embeddings: exploration, explanation, and exploitation](https://towardsdatascience.com/word-embeddings-exploration-explanation-and-exploitation-with-code-in-python-5dac99d5d795)
  (uses GloVe via Gensim)  
* [How to Develop Word Embeddings in Python with Gensim](https://machinelearningmastery.com/develop-word-embeddings-python-gensim/)
  (discusses pre-trained embeddings)
* [Word Embeddings with Gensim](https://becominghuman.ai/word-embeddings-with-gensim-68e6322afdca)
  (discusses pre-trained embeddings)
* [Getting Started with Word2Vec and GloVe in Python](https://textminingonline.com/getting-started-with-word2vec-and-glove-in-python)
  (uses Gensim)
  

**Resources covering word2vec**

* [Short Text Categorization using Deep Neural Networks and Word-Embedding Models](https://datawarrior.wordpress.com/2016/10/12/short-text-categorization-using-deep-neural-networks-and-word-embedding-models/) 
  (uses Gensim) 
* [Learn Word2Vec by implementing it in tensorflow](https://towardsdatascience.com/learn-word2vec-by-implementing-it-in-tensorflow-45641adaf2ac)
  (discusses query word embedding vectors)
* [Playing around with Word2Vec](https://medium.com/@shubhamagarwal328/playing-around-with-word2vec-natural-language-processing-ccd10a044b1)
  (discusses vector similarity, k-means clustering of similar words, uses Gensim)
* [Making sense of word2vec](https://rare-technologies.com/making-sense-of-word2vec/)
* [Word Embeddings in Python with Spacy and Gensim]()https://www.shanelynn.ie/word-embeddings-in-python-with-spacy-and-gensim/)
* [Sentiment Analysis of Movie Reviews: word2vec](https://recurrentnull.wordpress.com/2016/10/21/sentiment-analysis-of-movie-reviews-2-word2vec/)
* [word2vec tutorial tensorflow](http://adventuresinmachinelearning.com/word2vec-tutorial-tensorflow/)

  
**Resources covering Glove**

* [Glove Stanford NLP](http://www-nlp.stanford.edu/projects/glove/)
* (video) [GloVe - Python for Word Representation - PyCon APAC 2018](https://www.youtube.com/watch?v=Y8gKX5zMRyQ)
* [A Comprehensive Introduction to Word Vector Representations](https://medium.com/ai-society/jkljlj-7d6e699895c4)
  (discusses SVD)
* [GloVe: Global Vectors for Word Representation](https://blog.acolyer.org/2016/04/22/glove-global-vectors-for-word-representation/)
  (discusses Matrix factorization vs shallow-window methods)
* [Word vectorization using Glove](https://medium.com/@japneet121/word-vectorization-using-glove-76919685ee0b)
  (print the embeddings for the word “samsung”)
* [How to Use Words Co-Occurrence Statistics to Map Words to Vectors](https://iksinc.online/tag/co-occurrence-matrix/) 
  (with a vectors example [here](https://iksinc.online/2015/06/23/how-to-use-words-co-occurrence-statistics-to-map-words-to-vectors/#comment-395))
* [What is GloVe?](https://towardsdatascience.com/emnlp-what-is-glove-part-i-3b6ce6a7f970)


#### Related 

* General Overview of Word Embedding techniques
    * [A Brief History of Word Embeddings (and some clarifications)](https://www.gavagai.se/blog/2015/09/30/a-brief-history-of-word-embeddings/) 
      (includes links to frameworks)
    * [Deep Learning for Text](https://freecontent.manning.com/deep-learning-for-text/)
    * [Complete Guide to Word Embeddings](https://nlpforhackers.io/word-embeddings/) 
      (mentions t-SNE)
    * [An overview of word embeddings and their connection to distributional semantic models](http://blog.aylien.com/overview-word-embeddings-history-word2vec-cbow-glove/)
    * [Using word embeddings](https://jjallaire.github.io/deep-learning-with-r-notebooks/notebooks/6.1-using-word-embeddings.nb.html)
    * [Data Sets: Word Embeddings Learned from Tweets and General Data](https://arxiv.org/ftp/arxiv/papers/1708/1708.03994.pdf)
    * [Learning Word Vectors for Sentiment Analysis]()http://ai.stanford.edu/~ang/papers/acl11-WordVectorsSentimentAnalysis.pdf)
    * [Stop Using word2vec](https://multithreaded.stitchfix.com/blog/2017/10/18/stop-using-word2vec/)
    * [What can I do with word vectors?](https://radimrehurek.com/gensim/models/keyedvectors.html) (scroll down)
    

* Misc. 
    * [Load Pretrained glove vectors in python](https://stackoverflow.com/questions/37793118/load-pretrained-glove-vectors-in-python)
    * [How to use pretrained embeddings from Glove?](https://github.com/OpenNMT/OpenNMT-py/issues/210)
      (discusses initialisation of word vector when using pre-trained word vecs)
    * [text2vec R package](http://text2vec.org/glove-cli.html)
    * [GloVe vs word2vec revisited](http://dsnotes.com/post/glove-enwiki/)
      (uses text2vec R package)
    * [Word Vectors in the Eighteenth Century](https://dh2017.adho.org/abstracts/582/582.pdf)
  
* Books
    * [Co-occurrence and Recommendation](https://www.safaribooksonline.com/library/view/practical-machine-learning/9781491915707/ch04.html)
      (Practical Machine Learning: Innovations in Recommendation Chapter 4)
    * [Machine Learning for Text](http://www.charuaggarwal.net/Text-Learning.pdf)
      (discusses Glove gradient descent optimization in Chapter 10.4)

* Papers
    * [Extending the Scope of Co-occurrence Embedding](https://web.stanford.edu/class/cs224n/reports/2758144.pdf)
    * [Improving Distributional Similarity with Lessons Learned from Word Embeddings](http://www.aclweb.org/anthology/Q15-1016)
    * [Swivel: Improving Embeddings by Noticing What’s Missing](https://arxiv.org/pdf/1602.02215.pdf)
      (good description of optimization pseudocode)


* Algorithms
    * [An overview of gradient descent optimization algorithms](http://ruder.io/optimizing-gradient-descent/index.html#challenges)
    * [Stochastic gradient descent](https://am207.github.io/2017/wiki/gradientdescent.html#stochastic-gradient-descent)

* Slides

    * [Simple	Word	Vector	representa2ons:	word2vec,	GloVe](https://pdfs.semanticscholar.org/presentation/548c/0412f63ab096c89892d663c34f36da678c10.pdf)
    * [Word Embeddings](http://www.cs.virginia.edu/~kc2wc/teaching/NLP16/slides/07-WordEmbedding.pdf)
    * [Richard Socher slides](https://cs224d.stanford.edu/lectures/CS224d-Lecture3.pdf)

* Videos
    * [Coursera NLP](https://www.coursera.org/lecture/language-processing/distributional-semantics-bee-and-honey-vs-bee-an-bumblebee-PtRav)
    * [Coursera NLP (Andrew Ng)](https://www.coursera.org/lecture/nlp-sequence-models/glove-word-vectors-IxDTG)
    * [Coursera Intro to Deep Learning](https://www.coursera.org/lecture/intro-to-deep-learning/word-embeddings-dhzl5)
      (word2vec)
    * [word embeddings: what, how and whither](http://u.cs.biu.ac.il/~yogo/cvsc2015.pdf)

*Code Repos*

    * [Gensim](https://radimrehurek.com/gensim/models/word2vec.html)
      (includes word2vec and GloVe)
    * [glove-python](https://github.com/maciejkula/glove-python)
      (maciejkula)
    * [tf-glove](https://github.com/eschorn0/tf-glove)
      (Glove for Python, Cython and Tensorflow r1.0 on Ubuntu)
    * [glovepy](https://pypi.org/project/glovepy/)
      (A Python implementation with Cython of the GloVe)
    * [A GloVe implementation in Python](http://www.foldl.me/2014/glove-python/) (foldl)
    * [machine_learning_examples](https://github.com/lazyprogrammer/machine_learning_examples/tree/master/nlp_class2)
      (lazyprogrammer)
    * [movie sentiment](https://github.com/saurabhmathur96/movie-sentiment)

* Datasets

    * [Where to get pretrained models](https://github.com/3Top/word2vec-api#where-to-get-a-pretrained-models)







