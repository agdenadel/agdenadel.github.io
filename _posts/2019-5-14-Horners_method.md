---
layout: post
title: Horner's method
---

I recently came across Horner's method for the first time. It's a simple algorithm for evaluating polynomials at a point and is a good example of why we don't necessarily compute by using a definition directly (or by using the simplest method, or a method that is intuitive). For example: matrix operations (multiplications, inverses) are often done (under the hood) in ways that don't follow the definitions or methods you might learn in your first linear algebra class.

So what is Horner's method? If you have a polynomial \\(p\\), written as

$$p(x) = a_0 + a_1 x + a_2 x^2 + ... + a_n x^n$$

we could naively compute \\(p(x)\\) for a given value of \\(x\\) by simply plugging the value of \\(x\\) into this equation. What is the computational complexity of this algorithm? Without considering efficient ways of computing powers of a number, there are \\( n + (n-1) + (n-2) + ... + 2 + 1\\) multiplications (\\(n\\) for multiplying by the coefficients and the rest are for computing powers of \\(x\\)) and \\(n\\) additions.

If we're clever about how we rearrange things, we can reduce this to only \\(n\\) multiplications and \\(n\\) additions. Notice that 

$$p(x) = a_0 + a_1 x + a_2 x^2 + ... + a_n x^n$$

can be rewritten as

$$p(x) = a_0 + x (a_1 + x (a_2 + x(a_3 + ... + x(a_{n-1} + xa_n) ... ))).$$

This gives you a natural way to compute \\(p(x)\\) using \\(n\\) multiplications and \\(n\\) additions: you just compute directly starting with the most nested term. In a more explicit way, we define the following variables

$$b_n = a_n \\ b_{n-1} = a_{n-1} + b_n x \\ b_{n-1} = a_{n-2} + b_{n-1} x \\ \vdots \\b_0 = a_0 + b_1 x.$$

If we compare this sequence with the definition of \\(p(x)\\) we can see that \\(b_0 = p(x)\\). This gives us a nice way to evaluate polynomials efficiently.
