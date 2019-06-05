import numpy as np
import matplotlib.pyplot as plt


def square_uniform_sampling(num_samples):
    return np.random.uniform(low=[-1,-1], high=[1,1], size=(num_samples,2))


def point_in_circle(point):
    return point[0]**2 + point[1]**2 < 1


def get_points_in_circle(points):
    return points[list(map(point_in_circle, points))]


def circle_uniform_sampling(num_samples):
    square_points = square_uniform_sampling(num_samples)
    return get_points_in_circle(square_points)

def plot(data):
    plt.scatter(data[:,0], data[:,1])
    plt.show()


def main():
    num_samples = 1000
    square_samples = square_uniform_sampling(num_samples)
    plot(square_samples)
    circle_samples = circle_uniform_sampling(num_samples)
    plot(circle_samples)


if __name__ == "__main__":
    main()