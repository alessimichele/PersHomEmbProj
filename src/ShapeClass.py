import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Shape:
    """
    Base class for plotting 3D shapes.

    ---------
    Example:
    swissroll = SwissRoll(n=1000)
    swissroll.plot()

    cylinder = Cylinder(n=500)
    cylinder.plot()

    sphere = Sphere(n=1000, radius=2)
    sphere.plot()

    torus = Torus(n=800, r=1, R=3)
    torus.plot()

    circle = Circle(n=200)
    circle.plot()

    eight = Eight(n=300)
    eight.plot()
    """

    def __init__(self):
        self.n = None

    def plot(self):
        """
        Plots the shape in a 3D plot.
        """
        pass


class SwissRoll(Shape):
    """
    Class for generating and plotting a swiss roll shape.
    """

    def __init__(self, n):
        """
        Parameters:
        n : int
            Number of points to generate.
        """
        super().__init__()
        self.n = n

    def generate_data(self):
        """
        Generate data for the Swiss Roll shape.

        Returns:
        - data: numpy array of shape (n, 3) representing the coordinates of the points in the Swiss Roll shape.
        """
        data = np.zeros((self.n, 3))
        phi = np.random.uniform(low=1.5 * np.pi, high=4.5 * np.pi, size=self.n)
        psi = np.random.uniform(0, 10, self.n)

        data[:, 0] = phi * np.cos(phi)  # x coordinate
        data[:, 1] = phi * np.sin(phi)  # y coordinate
        data[:, 2] = psi  # z coordinate
        return data

    def plot(self):
        """
        Plot the Swiss Roll shape.
        """
        data = self.generate_data()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(data[:, 0], data[:, 1], data[:, 2], c="b", marker="o")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title("Swiss Roll")
        plt.show()


class Cylinder(Shape):
    """
    Class for generating and plotting a cylinder shape.
    """

    def __init__(self, n, radius=1, height=10):
        """
        Parameters:
        n : int
            Number of points to generate.
        radius : float, optional
            Radius of the cylinder. Default is 1.
        height : float, optional
            Height of the cylinder. Default is 10.
        """
        super().__init__()
        self.n = n
        self.radius = radius
        self.height = height

    def generate_data(self):
        """
        Generate data for the Cylinder shape.

        Returns:
        - data: numpy array of shape (n, 3) representing the coordinates of the points in the Cylinder shape.
        """
        data = np.zeros((self.n, 3))
        phi = np.random.uniform(low=0, high=2 * np.pi, size=self.n)
        psi = np.random.uniform(0, self.height, self.n)

        data[:, 0] = self.radius * np.cos(phi)  # x coordinate
        data[:, 1] = self.radius * np.sin(phi)  # y coordinate
        data[:, 2] = psi  # z coordinate
        return data

    def plot(self):
        """
        Plot the Cylinder shape.
        """
        data = self.generate_data()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(data[:, 0], data[:, 1], data[:, 2], c="r", marker="o")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title("Cylinder")
        plt.show()


class Sphere(Shape):
    """
    Class for generating and plotting a sphere shape.
    """

    def __init__(self, n, radius=1):
        """
        Parameters:
        n : int
            Number of points to generate.
        radius : float, optional
            Radius of the sphere. Default is 1.
        """
        super().__init__()
        self.n = n
        self.radius = radius

    def generate_data(self):
        """
        Generate data for the Sphere shape.

        Returns:
        - data: numpy array of shape (n, 3) representing the coordinates of the points in the Sphere shape.
        """
        data = np.zeros((self.n, 3))
        phi = np.random.uniform(low=0, high=2 * np.pi, size=self.n)
        psi = np.random.uniform(0, np.pi, self.n)

        data[:, 0] = self.radius * np.cos(phi) * np.sin(psi)  # x coordinate
        data[:, 1] = self.radius * np.sin(phi) * np.sin(psi)  # y coordinate
        data[:, 2] = self.radius * np.cos(psi)  # z coordinate
        return data

    def plot(self):
        """
        Plot the Sphere shape.
        """
        data = self.generate_data()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(data[:, 0], data[:, 1], data[:, 2], c="g", marker="o")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title("Sphere")
        plt.show()


class Torus(Shape):
    """
    Class for generating and plotting a torus shape.
    """

    def __init__(self, n, r=1, R=3):
        """
        Parameters:
        n : int
            Number of points to generate.
        r : float, optional
            Minor radius of the torus. Default is 1.
        R : float, optional
            Major radius of the torus. Default is 3.
        """
        super().__init__()
        self.n = n
        self.r = r
        self.R = R

    def generate_data(self):
        """
        Generate data for the Torus shape.

        Returns:
        - data: numpy array of shape (n, 3) representing the coordinates of the points in the Torus shape.
        """
        data = np.zeros((self.n, 3))
        phi = np.random.uniform(0, 2 * np.pi, size=self.n)
        psi = np.random.uniform(0, 2 * np.pi, size=self.n)

        data[:, 0] = (self.R + self.r * np.cos(phi)) * np.cos(psi)  # x coordinate
        data[:, 1] = (self.R + self.r * np.cos(phi)) * np.sin(psi)  # y coordinate
        data[:, 2] = self.r * np.sin(phi)  # z coordinate
        return data

    def plot(self):
        """
        Plot the Torus shape.
        """
        data = self.generate_data()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(data[:, 0], data[:, 1], data[:, 2], c="m", marker="o")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title("Torus")
        plt.show()


class Circle(Shape):
    """
    Class for generating and plotting a circle shape.
    """

    def __init__(self, n=100):
        """
        Parameters:
        n : int, optional
            Number of points to generate. Default is 100.
        """
        super().__init__()
        self.n = n

    def generate_data(self):
        """
        Generate data for the Circle shape.

        Returns:
        - data: numpy array of shape (n, 2) representing the coordinates of the points in the Circle shape.
        """
        data = np.zeros((self.n, 2))
        t = np.random.uniform(0, 2 * np.pi, size=self.n)
        data[:, 0] = np.sin(t)  # x coordinate
        data[:, 1] = np.cos(t)  # y coordinate
        return data

    def plot(self):
        """
        Plot the Circle shape.
        """
        data = self.generate_data()

        plt.scatter(data[:, 0], data[:, 1], c="y", marker="o")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Circle")
        plt.show()


class Eight(Shape):
    """
    Class for generating and plotting an eight shape.
    """

    def __init__(self, n=100):
        """
        Parameters:
        n : int, optional
            Number of points to generate. Default is 100.
        """
        super().__init__()
        self.n = n

    def generate_data(self):
        """
        Generate data for the Eight shape.

        Returns:
        - data: numpy array of shape (n, 2) representing the coordinates of the points in the Eight shape.
        """
        data = np.zeros((self.n, 2))
        t = np.random.uniform(0, 2 * np.pi, size=self.n)
        data[:, 0] = np.sin(t)  # x coordinate
        data[:, 1] = np.sin(t) * np.cos(t)  # y coordinate
        return data

    def plot(self):
        """
        Plot the Eight shape.
        """
        data = self.generate_data()

        plt.scatter(data[:, 0], data[:, 1], c="k", marker="o")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Eight")
        plt.show()
