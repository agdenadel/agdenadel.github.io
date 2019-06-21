---
layout: post
title: f-divergence
---

There are many applications of the information theoretic idea of **Kullback-Leibler divergence** (also known as KL-divergence and relative entropy). It is a measure of how one probability differs from another. Given two discrete probability distributions \\(p,q\\) defined on the same probability space, the KL-divergence, \\(D\\) between \\(p\\) and \\(q\\) is defined as

$$D_{KL}(p ||q) = -\sum_x p(x) \log \frac{q(x)}{p(x)} = \sum_x p(x) \log \frac{p(x)}{q(x)}$$

it can be analogously defined for continuous densities by

$$D_{KL}(f || g) = - \int_{-\infty}^{\infty} f(x) \log \frac{g(x)}{f(x)} dx$$

and can be defined in a measure-theoretic way for probability measures \\(P\\) and \\(Q\\) (assuming \\(P\\) is absolutely continuous with respect to \\(Q\\), which is essentially something we require for the other definitions as well) as

$$D_{KL}(P||Q) = - \int_X \frac{dP}{dQ} \log \frac{dP}{dQ} dQ$$

using the Radon-Nikodym derivative \\(P\\) with respect to \\(Q\\).

The KL-divergence has many nice properties and can be found widely in information theory, machine learning, and other fields. It turns out that some of these properties don't depend on the exact definition of KL-divergence, but actually rely on the fact that logarithms are concave. This encourages a natural extension of the KL-divergence.

## \\(f\\)-divergences

I'm going to defined \\(f\\)-divergences for density functions. Given a convex function \\(f\\) and two densities \\(g,h\\), an \\(f\\)-divergence is a function \\(D_f\\) defined

$$D_f(g||h) = \int_{-\infty}^{\infty} g(x) f \left(\frac{g(x)}{h(x)}\right) dx.$$

Many \\(f\\)-divergences are well-known by other names:

1. KL-divergence, \\(f(t) = t \log t\\)
2. Hellinger distance, \\(f(t) = (\sqrt{t} - 1)^2\\)
3. Total variation distance, \\(f(t) = \frac{1}{2} \|t-1\|\\)
4. Pearson \\(\chi^2\\)-divergence, \\(f(t) = (t-1)^2\\)

## Non-negativity

It's easy to show that KL-divergence is non-negative. The proof is basically just Jensen's inequality using the fact that negative logarithms are convex. Since this is true for any function that is convex, it is also true for all \\(f\\)-divergences.

## Significance

So why do we care about \\(f\\)-divergences when we already have the perfectly good KL-divergence? To be frank, I'm not really clear about this. What makes sense to me is that this generalization allows us to tailor our measure of divergence in customized ways that capture particular behavior that we may care about.

## Proofs of why KL-divergence isn't a metric

Another well-known fact about KL-divergence is that it is not symmetric which precludes it being used as a metric on a space of probability distributions (but it also doesn't satisfy the triangle inequality). We can show each of these two facts by finding counterexamples for each of them.

1. To see that KL-divergence isn't symmetric, consider \\(p=(1/2, 1/2)\\) and \\(q=(1/3, 2/3)\\). Then, by using the definition directly we get

$$D(p\|\|q) = \frac{1}{2} \log \frac{9}{8} \approx 0.08496$$

$$D(q\|\|p) = \frac{1}{3} \log \frac{2}{3} + \frac{2}{3} \log \frac{4}{3} \approx 0.08170$$

which are not equal.

2. To see that KL-divergence doesn't satisfy the triangle inequality, consider \\(p = (1/2, 1/2), q = (1/3, 2/3), r = (1/4, 3/4)\\). Then we have 

$$D_{KL}(p\|\|q) \approx 0.08496$$

$$D_{KL}(q\|\|r) \approx 0.02506$$

$$D_{KL}(p\|\|r) \approx 0.20752$$

which doesn't satisfy the triangle inequality.

3. Note that the KL-divergence is a premetric, which is a function satisfying

$$d(x,y) \geq 0$$
$$d(x,x) \geq 0$$

and can generate a topology on the space of probability distributions.

## Jensen-Shannon divergence

Since KL-divergence isn't a metric, it would be nice to have some other metric on probability distributions. The Jensen-Shannon divergence (also called the information radius or the total divergence to the average) helps us get this. It is defined as follows:

$$JSD(P||Q) = \frac{1}{2} D(P||M) + \frac{1}{2} D(Q||M)$$

where \\(M = \frac{1}{2}(P+Q)\\). We can see immediately that the Jensen-Shannon divergence is symmetric, which solves one issue that KL-divergence has. It turns out the the square root of the Jensen-Shannon divergence is actually a metric as well. Recall that for \\(d\\) to be a metric we need

1. \\(d(x,y) \geq 0\\)
2. \\(d(x,y) = 0\\) iff \\(x=y\\)
3. \\(d(x,y) = d(y,x)\\)
4. \\(d(x,z)  \leq d(x,y) + d(y,z)\\)

By properties of KL-divergence we have 1 and 2 and by symmetry we have 3 for both JSD and it's square root. We now need the triangle inequality. It doesn't hold for the JSD, but doe hold for its square root. The proof of this can be found in *A New Metric for Probability Distributions* by Dominik Endres and Johannes Schindelin

## Basic implementation

This is nowhere near a production implementation, but it is how I computed the counterexamples above. Notice that the logarithm is base two, this is generally standard for information theoretic concepts like KL divergence.

```python
import math


def log2(x):
    return math.log(x, 2)


def f_divergence(p, q, f):
    sum = 0
    for x,y in zip(p,q):
        sum += x * f(x/y)
    return sum


def kl_divergence(p, q):
    return f_divergence(p, q, log2)
```


## References

1. Elements of Information Theorey by Cover and Thomas
2. Information Theory, Inference, and Learning Algorithms by MacKay
3. [https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence)
4. [https://www.stat.berkeley.edu/~aditya/resources/STAT212aOverview.pdf](ttps://www.stat.berkeley.edu/~aditya/resources/STAT212aOverview.pdf)






