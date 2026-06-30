---
layout: post
title: Information Criteria
tags: linear_regression information_criteria information_theory
---

When I was an undergrad I took a course that covered linear regression and ANOVA in depth. We covered both theory and basic statistical computing in R (mostly how to use the models we learned in R). At some point in the course we discussed model selection: forward selection and backward elimination. In forward selection, you start with no variables in your model and greedily "improve" the model by adding one variable at a time. In backward elimination you start with a model including all possible variables and greedily "improve" the model by removing one variable at a time.

This description leaves some obvious questions. What does it mean to improve the model? How do we know when to stop? These are questions that need answering before you can use these methods for model selection.

## Linear regression

First, let's define our model. We have a collection of random samples \\( \{ (X_i, Y_i) \} \\) where each \\(Y_i\\) is the observation of the response variable and each \\(X_i\\) are the observations of multiple independent variables. We assume 

$$ Y_i = \beta_0 + \beta_1 X_{i1} + ... + \beta_p X_{ip} + \epsilon_i.$$

There are \\(n\\) total observations and \\(p\\) independent variables. I'm not going to go into how we determine the values each \\(\beta_j\\), but there are standard techniques like least squares, maximum likelihood, and Bayesian inference. The proportion of variance explained by the model is called the "coefficient of determination" and is denoted by \\(R^2\\). It ranges between 0 and 1, with 0 being no explanatory ability and 1 being perfect explanatory ability. Some of the variables we are using may not give us improved prediction accuracy when we use the model on out of sample data but are able to capture more of the variance within the training data (i.e. overfitting). 

This corresponds to models with additional variables having a higher \\(R^2\\), a metric of performance of the model. This inflation of the \\(R^2\\) value means that we need to come up with metrics that take into account this fact and punish models that use large numbers of variables.

Here are several possible metrics (that I remember learning about in my class):

1. Adjusted \\(R^2\\)
2. Akaike's information criterion (AIC)
3. Bayesian information criterion (BIC)
4. Mallow's \\(C_p\\)

## Adjusted \\(R^2\\)

The coefficient of determination is defined as 

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

where \\(SS_{res}\\) is the residual sum of squares and \\(SS_{tot}\\) is the total sum of squares. The adjusted \\(R^2\\) (denoted \\(\overline{R}^2\\) or \\(R^2_{adj}\\)) tries to deal with the issue of \\(R^2\\) increasing with added variables regardless of their actual relation to the dependent variable. It is defined as 

$$\overline{R}^2 = 1 - \frac{\frac{1}{n-p-1}SS_{res}}{\frac{1}{n-1}SS_{tot}}.$$

Notice that we are weighting the residual some of squares by the total number of observations reduced by the number of parameters and weighting the total by the number of observations. Also, notice that this ensures that adjusted \\(R^2\\) is always lower than \\(R^2\\). For additional justification of these weights, consider that one estimate of the variance is \\(SS_{res} / n\\) and \\(SS_{tot} / n\\). These are biased estimates the unbiased estimates of these variances is given by \\(SS_{res} / (n-p-1) \\) and \\(SS_{tot} / (n-1)\\).

## Information Criteria

Wikipedia has a long list of information criteria (along with other criteria for model selection):

* AIC
* BIC
* Deviance information criterion (DIC)
* Focused information criterion (FIC)
* Hannan-Quinn information criterion
* Watanabe-Akaike information criterion (WAIC)

Two of the most common are AIC and BIC.

### Akaike Information Criterion

The AIC was introduced by Hirotugu Akaike in the 1970s. It has a simple definition:

$$AIC = 2p - 2 log \hat{L}$$

where \\(p\\) is the number of parameters estimated and \\(\hat{L}\\) is the maximum value of the likelihood function for the model. 

### Bayesian Information Criterion

The BIC is also called the Schwarz information criterion (SIC, SBC, SBIC). It was introduced by Gideon E. Schwarz in the 1970s and it also has a simple definition:

$$BIC = log(n) p - 2 log \hat{L}$$

where \\(p\\) is the number of parameters estimated, \\(n\\) is the number of observations, and \\(\hat{L}\\) is the maximum value of the likelihood function for the model. Notice how the form of the BIC is very similar to the AIC.


## Mallow's \\(C_p\\)

This is another statistic used in a similar way to the AIC and BIC.


## Derivations

I think that in a later post I will write out the derivations of these statistics. When I was looking up the BIC derivation I read somewhere that the [original BIC paper](http://www.andrew.cmu.edu/user/kk3n/simplicity/schwarzbic.pdf) is quite readable. In addition, here is the [original AIC paper](https://ieeexplore.ieee.org/document/1100705).


