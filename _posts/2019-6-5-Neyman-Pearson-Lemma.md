---
layout: post
title: Neyman-Pearson Lemma
---


The Neyman-Pearson Lemma is a fundamental result in the theory of hypothesis testing and can also be restated in a form that is foundational to classification problems in machine learning. Even though the Neyman-Pearson lemma is a very important result, it has a simple proof. Let's go over the theorem and its proof.


## Performance of a classifier

Before stating the lemma, we need to know some basic metrics for judging the performance of a binary classifier. The binary classification problem is this: given an observation, \\(X\\) we want to predict the class of this observation, \\(Y \in \\{1,2\\}\\). A classifier is a function \\(h\\) that predicts the class of a given observation. There are four probabilities that we care about when predicting classes

$$P(h(X) = 1 | Y=1)$$

$$P(h(X) = 2 | Y=1)$$

$$P(h(X) = 1 | Y=2)$$

$$P(h(X) = 2 | Y=2)$$

There are different names for these probabilities. The Neyman-Pearson lemma is concerned with two of them. The first, \\(P(h(X)=2\|Y=2)\\), is often called the discovery rate (DR) or the power. We will call it the DR. The second, \\(P(h(X)=2\|Y=1)\\), is often called the false alarm rate (FAR) or Type I Error. We will call it the FAR. Notice that with the FAR and the DR we can easily determine the other probabilities (since two pairs must add up to 1).



## Neyman-Pearson Lemma

We are now ready to state the lemma. Denote the conditional densities \\(f(X\|Y=i) = f_i(x)\\). For \\(t > 0\\) define a classifier (with parameter \\(t\\)) by

$$h_t(x) = \begin{cases}
1 \text{ if } f_2(x) \leq t f_1(x) \\
2 \text{ if } f_2(x) > t f_2(x) 
\end{cases}.$$

Let \\(h(x) \rightarrow \\{1,2\\}\\) be any classification function. Then \\(DR(h) \leq DR(h_t)\\) if \\(FAR(h) \leq FAR(h_t)\\).

## Proof

First, we notice that we can partition the space into 4 parts:

$$A = \{ x : h(x) = h_t(x) = 2 \}$$

$$B = \{ x : h(x) = 2, h_t(x) = 1 \}$$

$$C = \{ x : h(x) = 1, h_t(x) = 2 \}$$

$$D = \{ x : h(x) = h_t(x) = 1 \}.$$

Then,

$$FAR(h) = P(h(X)=2|Y=1) = P(X \in A \cup B | Y = 1)$$

$$FAR(h_T) = P(h_(X)=2|Y=1) = P(X \in A \cup C | Y = 1).$$

By assumption, \\(FAR(h) \leq FAR(h_t)\\), so 

$$P(X \in A \cup B | Y = 1) \leq P(X \in A \cup C | Y = 1)$$

which implies

$$P(X \in B | Y = 1) \leq P(X \in C | Y = 1)$$

or equivalently

$$\int_B f_1(x) dx \leq \int_C f_1(x) dx.$$

By the definitions of \\(h_t, B, C\\) we have that \\(f_2 \leq t f_1\\) on \\(B\\) and \\(f_2 > t f_1\\) on \\(C\\). From this we know 

$$P(X \in B | Y = 2) = \int_B f_2(x) dx$$

$$ \leq t \int_B f_1(x) dx$$

$$ \leq \int_C t f_1(x) dx$$

$$ \leq \int_C f_2(x) dx$$

$$ = P(X \in C | Y = 2).$$

Applying this result, we have

$$DR(h) = P(h(x) =2 | Y=2)$$

$$ = P(X \in A \cup B| Y = 2)$$

$$ \leq  P(X \in A \cup C| Y = 2)$$

$$ = P(h_t(X) = 2 | Y = 2)$$

$$ = DR(h_t).$$

This is what we wanted to prove.



## Hypothesis testing

When thinking about hypothesis tests, the Neyman-Pearson lemma applies to tell us that a likelihood ratio test is the the most powerful hypothesis test for a given significance level \\(\alpha\\). The reason why likelihood ratio tests aren't the only tests we use is that the relationship between \\(\alpha\\) and \\(t\\) is not always clear (i.e. we don't always know how to calibrate the test).



## Generalization

Something I'm interested in looking into is the sequential probability ratio test. This is a generalization of the Neyman-Pearson lemma for sequential hypothesis testing (sequential analysis). Here are a few links if this interests you:

1. [https://en.wikipedia.org/wiki/Sequential_analysis](https://en.wikipedia.org/wiki/Sequential_analysis)
2. [https://en.wikipedia.org/wiki/Sequential_probability_ratio_test](https://en.wikipedia.org/wiki/Sequential_probability_ratio_test)
3. [https://www.evanmiller.org/sequential-ab-testing.html](https://www.evanmiller.org/sequential-ab-testing.html)



