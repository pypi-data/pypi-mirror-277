"""This module contains the geometry classes for the area of interest."""

import numpy as np


class RectGeom:
    """
    Rectangular geometry based on 4 corner points and a resolution step.

    Attributes:
    - xi (float): x-coordinate of the lower-left corner.
    - xf (float): x-coordinate of the upper-right corner.
    - yi (float): y-coordinate of the lower-left corner.
    - yf (float): y-coordinate of the upper-right corner.
    - resolution (float): resolution step for the grid.
    - grid_x (numpy.ndarray): 2D grid of x-coordinates.
    - grid_y (numpy.ndarray): 2D grid of y-coordinates.
    - dim_x (int): Number of cells along the x-axis.
    - dim_y (int): Number of cells along the y-axis.
    """

    def __init__(self, geometry_corners):
        """
        Initialize the geometry based on the 4 corners and the resolution.

        Parameters:
        - geometry_corners (list): List of 5 floats representing the 4 corner
        points (xi, xf, yi, yf) and the resolution step.

        This method initializes the rectangular geometry using the provided corner
        points and resolution step. It calculates the grid of x and y coordinates
        based on the corner points and resolution step. Additionally, it computes
        the dimensions of the grid.
        """
        self.xi = geometry_corners[0]
        self.xf = geometry_corners[1]
        self.yi = geometry_corners[2]
        self.yf = geometry_corners[3]
        self.resolution = geometry_corners[4]

        self.grid_x, self.grid_y = np.mgrid[
            self.xi : self.xf + self.resolution : self.resolution,
            self.yi : self.yf + self.resolution : self.resolution,
        ]

        self.dim_x = self.grid_x.shape[0]
        self.dim_y = self.grid_x.shape[1]

    def find_nearest_node(self, x, y):
        """
        Find the nearest node in the grid to the given coordinates.

        Parameters:
        - x (float): The x-coordinate of the point.
        - y (float): The y-coordinate of the point.

        Returns:
        - numpy.ndarray: An array containing the indices of the nearest node
        in the grid.

        This method calculates the indices of the nearest node in the grid to
        the given coordinates (x, y). It first computes the indices of the grid
        cell containing the point using floor division and adjusting for grid
        resolution and origin. The result is returned as a NumPy array with
        shape (2,) representing the row and column indices of the nearest node.
        """
        idx_x = np.floor((x + self.resolution / 2 - self.xi) / self.resolution).astype(
            int
        )
        idx_y = np.floor((y + self.resolution / 2 - self.yi) / self.resolution).astype(
            int
        )
        return np.column_stack((idx_x, idx_y))
