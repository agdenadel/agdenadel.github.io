---
layout: post
title: Law of Total Variance
tags: probability proof
---

Remember the Law of Total Expectation (also called the Tower Property)? It states

$$\mathbb{E}[Y] = \mathbb{E}[\mathbb{E}[Y|X]].$$

The proof is straightforward in the discrete case (use the definition to expand in terms of \\(\mathbb{P}(Y=y\|X=x)\\) and justify swapping the order of summation) and in the general (i.e. measure theoretic) case is an exercise in using the definition of conditional expectation as a Radon-Nikodym derivative and using measurability properties. The [Wikipedia page](https://en.wikipedia.org/wiki/Law_of_total_expectation) has both proofs.

There's a similar rule that allows you to decompose the variance of a random variable called the Law of Total Variance

$$\text{Var}(Y) = \mathbb{E}[\text{Var}(Y|X)] + \text{Var}(\mathbb{E}[Y|X]).$$

The proof relies on the Law of Total Expectation, the definition of conditional variance, and the fact that \\(\text{Var}(Y) = \mathbb{E}[Y^2] + \mathbb{E}[Y]^2\\). Consider

$$\text{Var}(Y) = \mathbb{E}[Y^2] - \mathbb{E}[Y]^2]$$

and applying the Law of Total Expectations to both terms yields

$$ = \mathbb{E}[\mathbb{E}[Y^2|X]] - \mathbb{E}[\mathbb{E}[Y|X]]^2$$

adding and subtracting \\(\mathbb{E}[Y\|X]^2 \\) yields

$$ = \mathbb{E}[\mathbb{E}[Y^2|X] - \mathbb{E}[Y|X]^2 + \mathbb{E}[Y|X]^2] - \mathbb{E}[\mathbb{E}[Y|X]]^2$$

and noticing the [definition of conditional variance](https://en.wikipedia.org/wiki/Conditional_variance)

$$ = \mathbb{E}[\text{Var}(Y|X)] + \mathbb{E}[\mathbb{E}[Y|X]^2] - \mathbb{E}[\mathbb{E}[Y|X]]^2$$

and, finally, noticing the definition of the variance of a random variable (where the random variable of interest is \\(\mathbb{E}[Y\|x]\\)) yields the Law of Total Variance

$$ = \mathbb{E}[\text{Var}(Y|X)] + \text{Var}(\mathbb{E}[Y|X]).$$


