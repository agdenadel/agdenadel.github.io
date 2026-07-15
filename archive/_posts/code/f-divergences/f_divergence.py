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

if __name__ == "__main__":
    p = [1/2, 1/2]
    q = [1/3, 2/3]
    r = [1/4, 3/4]

    print(kl_divergence(p,q))
    print(kl_divergence(q,r))
    print(kl_divergence(p,r))