---
layout: post
title: Sicherman Dice
---


[Sicherman dice](https://en.wikipedia.org/wiki/Sicherman_dice) are a "relabeling" of a standard pair of dice in such a way that their sum has the same distribution as a standard pair of dice. While a standard pair of dice is labeled with (1,2,3,4,5,6) on each of the two dice, Sicherman dice are labeled with (1,2,2,3,3,4) and (1,3,4,5,6,8). It's left as an exercise to the reader to confirm that this relabeling has the same distribution as a standard pair of dice :)

I first learned about Sicherman dice when I was an undergrad. I learned about them from Tom Edgar, my advisor at PLU, during a topics course he taught on enumerative combinatorics.

Tom taught the course with what he called the modified Moore method. Every few weeks he would hand out a list of problems (a "chapter"). The job of the students was to take the problems home, look them over, and try to solve them. We would then present our solutions in class to each other. Tom did minimal lecturing and only rarely presented a problem himself. Each chapter was on a different set of techniques in combinatorics. We started with the very basics of counting using combinations and permutations and worked our way up to more sophisticated techniques, like generating functions. Generating functions are the technique we can use to generate the Sicherman dice.

The generating function for a die is 

$$ x + x^2 + x^3 + x^4 + x^5 + x^6 $$

and the generating function for a pair of dice is 

$$ (x + x^2 + x^3 + x^4 + x^5 + x^6) = x^12 + 2*x^11 + 3*x^10 + 4*x^9 + 5*x^8 + 6*x^7 + 5*x^6 + 4*x^5 + 3*x^4 + 2*x^3 + x^2.$$

In case you're curious, I didn't do this by hand. You can use the following Sage code (the [SageCell server](https://sagecell.sagemath.org/) can be really useful for running snippets of code like this):

~~~~
var('x')
expand((x + x^2 + x^3 + x^4 + x^5 + x^6)^2)
~~~~

How does this help us get the Sicherman dice? It turns out that you can factorize the generating function as follows:

~~~~
var('x')
factor(x^12 + 2*x^11 + 3*x^10 + 4*x^9 + 5*x^8 + 6*x^7 + 5*x^6 + 4*x^5 + 3*x^4 + 2*x^3 + x^2)
~~~~

Which gives you

$$(x^2 + x + 1)^2*(x^2 - x + 1)^2*(x + 1)^2*x^2.$$

This doesn't quite give us the Sicherman dice. We need a split this factorization into two parts: each being a polynomial with coefficients that sum to 6 whose product is the same as the generating function for the pair of normal dice. We can decompose the factorization above as follows

$$x (x+1) (x^2 + x + 1) = x + 2x^2 + 2x^3 + x^4$$

and

$$x(x+1)(x^2 + x +1)(x^2 - x + 1)^2 = x + x^3 + x^4 + x^5 + x^6 + x^8.$$

This is the only way to do this (you can check alternative choices for which factors you choose). 
