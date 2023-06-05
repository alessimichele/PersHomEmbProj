import matplotlib.pyplot as plt
import numpy as np
from persim import plot_diagrams
from sklearn.decomposition import PCA
from ripser import ripser


class PhomPCA:
    """
    PhomPCA is a class that performs persistent homology-based dimensionality reduction using PCA or kernel PCA.

    It allows for embedding the data by adding dimensions and reconstructing the data using PCA or kernel PCA.
    The class also computes the persistence diagrams for both the original and reconstructed data.
    Finally, it provides methods to visualize the persistence diagrams.

    """

    def __init__(self, original_data):
        """
        Initialize the PhomPCA class.

        Args:
        -----
        - original_data: numpy array of the original data

        Attributes:
        -----------
        - original_data: numpy array of the original data
        - n_points: number of data points
        - original_dim: dimensionality of the original data
        - augmented_data: augmented data with added dimensions
        - reconstructed_data: reconstructed data after dimensionality reduction
        - dgms: persistence diagrams for original data
        - dgms_reconstructed: persistence diagrams for reconstructed data

        """
        self.original_data = original_data
        self.n_points = original_data.shape[0]
        self.original_dim = original_data.shape[1]

        self.augmented_data = None
        self.reconstructed_data = None

        self.dgms = None
        self.dgms_reconstructed = None

    def embedding(self, N=20, noise=True, shuffle=False):
        """
        Perform embedding by adding dimensions to the original data.

        Args:
        ----
        - N: number of dimensions to add (default: 20)
        - noise: whether to add random noise (default: True)
        - shuffle: whether to shuffle the data (default: False)

        """
        # N: number of dimension to add
        if noise == True:
            noise_data = np.random.uniform(
                low=0.1 * self.original_data.min(),
                high=0.1 * self.original_data.max(),
                size=(self.n_points, N),
            )
            self.augmented_data = np.c_[self.original_data, noise_data]
        else:
            self.augmented_data = np.c_[
                self.original_data, np.zeros((self.n_points, N))
            ]

    def reconstruction(self, kernel=False):
        """
        Perform dimensionality reduction using PCA or kernel PCA.

        Args:
        ----
        - kernel: whether to use kernel PCA (default: False)

        """
        if kernel == False:
            from sklearn.decomposition import PCA

            pca = PCA(n_components=self.original_dim)
            self.reconstructed_data = pca.fit_transform(self.augmented_data)
        else:
            from sklearn.decomposition import KernelPCA

            kpca = KernelPCA(n_components=self.original_dim, kernel="rbf")
            self.reconstructed_data = kpca.fit_transform(self.augmented_data)

    def compute_pers_diag(self):
        """
        Compute the persistence diagrams for both original and reconstructed data.

        """
        self.dgms = ripser(self.original_data, maxdim=2)["dgms"]
        self.dgms_reconstructed = ripser(self.reconstructed_data, maxdim=2)["dgms"]

    def plot(self, save=False, title=False):
        """
        Plot the persistence diagrams for original and reconstructed data.

        Args:
        ----
        - save: whether to save the plot (default: False)
        - title: whether to add a title to the plot (default: False)

        """
        if save == True:
            fname = input("Enter file name: ")

        if title == True:
            tname = input("Enter title name: ")

        if self.original_dim == 3:
            # Create a figure with three subplots arranged in a row
            fig, axes = plt.subplots(3, 2, figsize=(10, 10))

            # Plot the first diagram
            plot_diagrams(self.dgms, ax=axes[0, 0], plot_only=[0])
            axes[0, 0].set_title(r"$H_0$ original data")

            plot_diagrams(self.dgms_reconstructed, ax=axes[0, 1], plot_only=[0])
            axes[0, 1].set_title(r"$H_0$ recostructed data")

            # Plot the second diagram
            plot_diagrams(self.dgms, ax=axes[1, 0], plot_only=[1])
            axes[1, 0].set_title(r"$H_1$ original data")

            plot_diagrams(self.dgms_reconstructed, ax=axes[1, 1], plot_only=[1])
            axes[1, 1].set_title(r"$H_1$ recostructed data")

            # Plot the third diagram
            plot_diagrams(self.dgms, ax=axes[2, 0], plot_only=[2])
            axes[2, 0].set_title(r"$H_2$ original data")

            plot_diagrams(self.dgms_reconstructed, ax=axes[2, 1], plot_only=[2])
            axes[2, 1].set_title(r"$H_2$ recostructed data")

            # Adjust spacing between subplots
            plt.tight_layout()

            if title == True:
                fig.suptitle(f"{tname}")

            if save == True:
                plt.savefig(f"./images/{fname}.png")

            # Display the plot
            plt.show()

        elif self.original_dim == 2:
            # Create a figure with three subplots arranged in a row
            fig, axes = plt.subplots(2, 2, figsize=(10, 10))

            # Plot the first diagram
            plot_diagrams(self.dgms, ax=axes[0, 0], plot_only=[0])
            axes[0, 0].set_title(r"$H_0$ original data")

            plot_diagrams(self.dgms_reconstructed, ax=axes[0, 1], plot_only=[0])
            axes[0, 1].set_title(r"$H_0$ recostructed data")

            # Plot the second diagram
            plot_diagrams(self.dgms, ax=axes[1, 0], plot_only=[1])
            axes[1, 0].set_title(r"$H_1$ original data")

            plot_diagrams(self.dgms_reconstructed, ax=axes[1, 1], plot_only=[1])
            axes[1, 1].set_title(r"$H_1$ recostructed data")

            if title == True:
                fig.suptitle(f"{tname}")

            if save == True:
                plt.savefig(f"./images/{fname}.png")

            plt.show()
