import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Shape:
    def __init__(self):
        self.n = None

    def plot(self):
        pass


def swiss_roll(n):
    """
    Parameters:
    n: int
        Number of points to generate
    """

    data = np.zeros((n, 3))
    phi = np.random.uniform(low=1.5 * np.pi, high=4.5 * np.pi, size=n)
    psi = np.random.uniform(0, 10, n)

    data[:, 0] = phi * np.cos(phi)  # x coordinte
    data[:, 1] = phi * np.sin(phi)  # y coordinate
    data[:, 2] = psi  # z coordinate
    return data


def cylinder(n, radius=1, height=10):
    """
    Parameters:
    n: int
        Number of points to generate
    """

    data = np.zeros((n, 3))
    phi = np.random.uniform(low=0, high=2 * np.pi, size=n)
    psi = np.random.uniform(0, height, n)

    data[:, 0] = radius * np.cos(phi)  # x coordinte
    data[:, 1] = radius * np.sin(phi)  # y coordinate
    data[:, 2] = psi  # z coordinate
    return data


def sphere(n, radius=1):
    """
    Parameters:
    n: int
        Number of points to generate
    """

    data = np.zeros((n, 3))
    phi = np.random.uniform(low=0, high=2 * np.pi, size=n)
    psi = np.random.uniform(0, np.pi, n)
    radius = radius

    data[:, 0] = radius * np.cos(phi) * np.sin(psi)  # x coordinte
    data[:, 1] = radius * np.sin(phi) * np.sin(psi)  # y coordinate
    data[:, 2] = radius * np.cos(psi)  # z coordinate
    return data


def torus(n, r=1, R=3):
    data = np.zeros((n, 3))
    phi = np.random.uniform(0, 2 * np.pi, size=n)
    psi = np.random.uniform(0, 2 * np.pi, size=n)

    # Calculate the x, y, and z coordinates of the torus
    data[:, 0] = (R + r * np.cos(phi)) * np.cos(psi)
    data[:, 1] = (R + r * np.cos(phi)) * np.sin(psi)
    data[:, 2] = r * np.sin(phi)

    return data


def circle(n=100):
    from sklearn import datasets

    data = (
        datasets.make_circles(n_samples=n)[0]
        + 5 * datasets.make_circles(n_samples=n)[0]
    )
    return data


def eight(n=100):
    t = np.random.uniform(0, 2 * np.pi, size=n)
    data = np.zeros((n, 2))
    data[:, 0] = np.sin(t)
    data[:, 1] = np.sin(t) * np.cos(t)
    return data
