---
layout: post
title: Anscombe's Quartet
---

Anscombe's quartet is an interesting collection of four datasets that have nearly identical metrics when modeled using simple linear regression. Here are the four datasets:

|      1      |      2      |      3      |      4      |
|------|------|------|------|------|------|------|------|
|  x   |  y   |   x  |   y  |   x  |   y  |   x  |   y  |
|------|------|------|------|------|------|------|------|
| 10.0 | 8.04 | 10.0 | 9.14 | 10.0 | 7.46 |  8.0 | 6.58 |
|  8.0 | 6.95 |  8.0 | 8.14 |  8.0 | 6.77 |  8.0 | 5.76 |
| 13.0 | 7.58 | 13.0 | 8.74 | 13.0 |12.74 |  8.0 | 7.71 |
|  9.0 | 8.81 |  9.0 | 8.77 |  9.0 | 7.11 |  8.0 | 8.84 |
| 11.0 | 8.33 | 11.0 | 9.26 | 11.0 | 7.81 |  8.0 | 8.47 |
| 14.0 | 9.96 | 14.0 | 8.10 | 14.0 | 8.84 |  8.0 | 7.04 |
|  6.0 | 7.24 |  6.0 | 6.13 |  6.0 | 6.08 |  8.0 | 5.25 |
|  4.0 | 4.26 |  4.0 | 3.10 |  4.0 | 5.39 | 19.0 | 12.5 |
| 12.0 |10.84 | 12.0 | 9.13 | 12.0 | 8.15 |  8.0 | 5.56 |
|  7.0 | 4.82 |  7.0 | 7.26 |  7.0 | 6.42 |  8.0 | 7.91 |
|  5.0 | 5.68 |  5.0 | 4.74 |  5.0 | 5.73 |  8.0 | 6.89 |


Notice that datasets 1-3 have the same \\(x\\) values, with varying \\(y\\) values. Let's plot the data and check some of these metrics. First, here is an image of the four datasets plotted in scatterplots. 

![Scatterplots for Anscombe's quartet](/images/anscombes_quartet.png)

Also, here is a Python script that plots the data, computes some basic metrics, and computes the linear regression model for each dataset.

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.stats import pearsonr
from sklearn.linear_model import LinearRegression


# Set up Anscombe's quartet data
x1 = x2 = x3 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])


# Take a look at the datasets
fig, ax = plt.subplots(2, 2)

ax[0,0].scatter(x1,y1)
ax[0,1].scatter(x2,y2)
ax[1,0].scatter(x3,y3)
ax[1,1].scatter(x4,y4)


# Means and variances of x are exactly equal
print("Means of x's")
print(np.mean(x1))
print(np.mean(x4))
print("Variances of x's")
print(np.var(x1))
print(np.var(x4))


# Means of y are equal to 2 decimal places
# The value is approximately 7.50
print("Means of y's")
print(np.mean(y1))
print(np.mean(y2))
print(np.mean(y3))
print(np.mean(y4))


# Variances of y are equal to 2 decimal places (rounded)
# The value is approximately 3.75
print("Variances of y's")
print(np.var(y1))
print(np.var(y2))
print(np.var(y3))
print(np.var(y4))


# Correlation between x and y is equal to 3 decimal places
# The value is approximately 0.816
print("Correlation")
print(pearsonr(x1,y1)[0])
print(pearsonr(x2,y2)[0])
print(pearsonr(x3,y3)[0])
print(pearsonr(x4,y4)[0])


# Linear regression is the same to 2 decimal places
model1 = LinearRegression()
model2 = LinearRegression()
model3 = LinearRegression()
model4 = LinearRegression()

model1.fit(x1.reshape(-1,1),y1)
model2.fit(x2.reshape(-1,1),y2)
model3.fit(x3.reshape(-1,1),y3)
model4.fit(x4.reshape(-1,1),y4)

# They each yield the line y = 3x + 0.5 (approximately)
print("Regression coefficients")
print(model1.intercept_, model1.coef_)
print(model2.intercept_, model2.coef_)
print(model3.intercept_, model3.coef_)
print(model4.intercept_, model4.coef_)
```
