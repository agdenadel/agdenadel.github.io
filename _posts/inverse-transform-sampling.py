import numpy as np
import matplotlib.pyplot as plt


def quantile_exponential_distribution(lambda_param, y):
    return -np.log(1-y) / lambda_param


def main():
    n = 10000
    exponential_samples = np.random.exponential(1,n)
    plt.hist(exponential_samples)
    plt.show()

    uniform_samples = np.random.uniform(0,1,n)
    plt.hist(uniform_samples)
    plt.show()

    transformed_exponential_samples = quantile_exponential_distribution(lambda_param=1, y=uniform_samples)
    plt.hist(transformed_exponential_samples)
    plt.show()


if __name__ == "__main__":
    main()