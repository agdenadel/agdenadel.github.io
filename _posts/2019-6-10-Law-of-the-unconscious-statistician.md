---
layout: post
title: Law of the Unconscious Statistician
tags: probability
---

The Law of the Unconscious Statistician is something that I'm pretty sure I've used before, but I'm not sure that I've ever proved. The law is a theorem that states

$$E[g(X)] = \int_{\mathbb{R}} g(x) f_X (x) dx$$

where \\(g\\) is some function and \\(X\\) is a random variable with density \\(f_X\\). Similarly, if \\(X\\) is a discrete random variable 

$$E[g(X)] = \sum_x  g(x) p_X (x) dx$$

where \\(X\\) has pmf \\(p_X\\). The theorem gets its name from the fact that many people apply this result without having proved it. This is presumably because it seems very intuitive and people often mistake this for the definition of the expectation of \\(E[g(X)]\\) without realizing that the definition of expectation involves the pdf (or pmf) of \\(g(X)\\) not \\(f_X\\) (i.e. if we use the definition we would have \\(E[g(X)] = \int_{\mathbb{R}} y f_Y(y) dy\\) where \\(Y = g(X)\\)). Let's prove this theorem.

## Proof

### Discrete case

The discrete case is the most straightforward. Consider

$$ E[g(X)] = \sum_y y p_Y (y)$$

substitute the definition of \\(p_Y\\)

$$ = \sum_y y P(g(X) = y) $$

use the definition of \\(g\\)

$$ = \sum_y y \sum_{x : g(x) = y} p_X (x) $$

use the fact that \\(y = g(x)\\) and re-index 

$$ = \sum_{x} g(x) p_X(x).$$ 


### Continuous case

To prove the continuous case, we need a little result from calculus (which looks a little complicated at first glance, but is very simple to derive).

#### Lemma (Inverse Function Theorem)

Given \\(y = f(x)\\) and assuming \\(f^{-1}\\) exists, we have

$$f'(x) = \frac{1}{(f^{-1})'(f(x))}.$$

#### Proof of lemma

By assumption we have \\(x = f^{-1}(y) = f^{-1}(f(x))\\). Differentiating yields

$$1 = (f^{-1})'(f(x)) f'(x).$$

which is equivalent to the desired result

$$f'(x) = \frac{1}{(f^{-1})'(f(x))}.$$

#### Proof of continuous case

The continuous case follows from a change of variable and applying the lemma. We'll work in the opposite direction of the discrete case. Notice that x = g^{-1}(y). From the lemma we have that

$$dx = \frac{1}{g'(g^{-1}(y))} dy.$$

Using this fact we can do a change of variables (also known as a substitution or a \\(u\\)-substitution) to obtain

$$\int_{-\infty}^{\infty} g(x) f_X(x) dx = \int_{-\infty}^{\infty} y f_X(g^{-1}(y)) \frac{1}{g'(g^{-1}(y))} dy.$$

Then, consider the following fact about the cdf of \\(Y\\) and its relation to the cdf of \\(X\\)

$$F_Y(y) = P(Y \leq y) = P(g(X) \leq y) = P(X \leq g^{-1}(y)) = F_X(g^{-1}(y)).$$

Then, differentiating to obtain the pdf yields

$$f_Y(y) = f_X(g^{-1}(y)) \frac{1}{g'(g^{-1}(y))}.$$

Combining this with our integral above yields

$$\int_{-\infty}^{\infty} g(x) f_X(x) dx = \int_{-\infty}^{\infty} g(x) f_X(x) dx = E[g(X)].$$


### Measure theoretic version

The measure theoretic version requires a bit more knowledge of measure theoretic probability. I think I'll break this out into a separate post (maybe with the background required).
