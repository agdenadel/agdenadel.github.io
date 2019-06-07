import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import seaborn as sns


def two_component_mixture_pdf(x):
    return (scipy.stats.norm.pdf(x, loc=-1, scale=0.5) + scipy.stats.norm.pdf(x, loc=1, scale=0.5))/2


def proposal_pdf(x):
    return scipy.stats.norm.pdf(x, loc=0, scale=2)


def two_component_mixture(num_samples, mixture_proportion=0.5):
    # generate mixture distribution
    component1_proportion = mixture_proportion
    component2_proportion = 1 - component1_proportion

    component1 = scipy.stats.norm.rvs(loc=-1, scale=0.5, size=int(num_samples * component1_proportion))
    component2 = scipy.stats.norm.rvs(loc=1, scale=0.5, size=int(num_samples * component2_proportion))

    data = np.append(component1, component2)
    return data


def sample_from_proposal():
    return scipy.stats.norm.rvs(loc=0, scale=2)


def rejection_sampling(num_samples, density_of_interest, proposal_density, envelope_constant):
    data = []
    i = 0
    while i != num_samples:
        x = sample_from_proposal()
        u = scipy.stats.uniform.rvs()

        if u < density_of_interest(x) / (envelope_constant * proposal_density(x)):
            data.append(x)
            i += 1

    return np.array(data)


def plot_densities():
    x = np.linspace(scipy.stats.norm.ppf(0.01, loc=0, scale=2), scipy.stats.norm.ppf(0.99, loc=0, scale=2), 100)
    
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].plot(x, proposal_pdf(x))
    ax[0].plot(x, two_component_mixture_pdf(x))
    ax[1].plot(x, proposal_pdf(x)*2.5)
    ax[1].plot(x, two_component_mixture_pdf(x))
    plt.show()


def main():
    num_samples = 10000
    direct_samples = two_component_mixture(num_samples)

    # envelope constant was found by inspection of plots and is not optimal
    envelope_constant = 2.5

    plot_densities()

    data = rejection_sampling(num_samples, two_component_mixture_pdf, proposal_pdf, 2.5)
    sns.distplot(direct_samples)
    plt.show()
    sns.distplot(data)
    plt.show()


if __name__ == "__main__":
    main()