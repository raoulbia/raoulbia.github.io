Title: Probabilities
Date: 2017-10-28
Category: Probabilities
Slug: Probabilities
Summary: Probabilities

<br>

#### Conditional probability refresher

$P(A|B) = \frac{P(A \cap B)}{P(B)}$

likewise

$P(B|A) = \frac{P(A \cap B)}{P(A)}$

this implies that:

$P(A \cap B) = P(A|B)P(B) = P(B|A)P(A)$

dividing both sides by P(B) gives us Bayes Theorem:

$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$

<br>

#### Events A **and** B occur: $P(A \cap B)$

Rule: Multiplication

Question: are those events dependent or independent?

<br>

*Independent Events*

$P(A \cap B) = P(A) \ \cdot P(B)$
  
Example: Roll two dice and get two Heads

* $P(H \cap H)$ = 0.5 * 0.5 = 0.25

<br>
    
*Dependent Events*

$P(A \cap B) = P(B)P(A|B) = P(A)P(B|A)$

Example: Pick two cards (wo/replacement) and get two Queens

* $P(Q1 \cap Q2) = P(Q1)P(Q2|Q1)$ = 4/52 * 3/51  

<br>

#### Either A **or** B or both occur: $P(A \cup B)$

Rule: Addition

Question: are those events mutually exlusive?

<br>

*Mutually exclusive events*

$P(A \cup B) = P(A) \ + \ P(B)$

Example: Roll a dice and get a 2 or a 5?

* $P(A \cup B) = P(A) \ + \ P(B)$ = 1/6 +1/6

<br>
  
*Events have common outcomes*

$P(A \cup B) = P(A) \ + \ P(B) \ - \ P(A \cap B)$

Example: Pick one card and get a King or Hearts

* $P(A \cup B) = P(K) \ + \ P(Hearts) \ - \ P(K of Hearts)$ = 4/52 + 13/52 - 1/52 

<br>
  
#### Probabilities involving "at least one" success

* Toss a coin two times: "*find the probability of getting at least one head*"
  <br> Note: these are independent events...  

\begin{align}
\text{P(at least one H)} &= 1 - \text{P(no Head)} \\
                       &= 1 - P(T \cap T) \\
                       &= 1 - P(T) * P(T) \\    
                       &= 1 - 0.25 = 0.75 
\end{align}

<br>
  
#### Binomial Probability "At Most" and "At Least"

* A bag contains 6 red Bingo chips, 4 blue Bingo chips, and 7 white Bingo chips. 
What is the probability of drawing a red Bingo chip at least 3 out of 5 times? 

<br>

#### Frechet Bounds

Suppose we know the values of Pr(A) and Pr(B), but no information is available regarding 
the joint event $(A \cap B)$.

The Frechet bounds are useful to define an interval for the probability of the
joint event $(A \cap B)$ when only information about the marginal
probabilities Pr(A) and Pr(B) is available.

$$max{Pr(A) + Pr(B) − 1, 0} \geq Pr(A \ B) \leq min{Pr(A), Pr(B)}$$

Example: Physiotherapists’ know that patients suffering from a particular type of
low back pain have the following trait probabilities:

* P(Pain at night) = 0.63
* P(Nerve injury) = 0.43

