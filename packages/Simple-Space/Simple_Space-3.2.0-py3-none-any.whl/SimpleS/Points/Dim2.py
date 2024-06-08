#in the name of GOD##
import numpy as np
import matplotlib.pyplot as plt
from SimpleS.utils import save_path_generator


def calculate_distance_between_two_points(A, B):
    """
    Calculate the distance of two points using formula derived from the Pythagorean theorem.
    Args:
    A, B (tuple): Points. A = (x1, y1), B = (x2, y2)
    Returns:
    float: Distance of the points.
    """
    x1, y1 = A
    x2, y2 = B
    # Distance = sqrt( (x2-x1)^2 + (y2-y1)^2 )
    return np.sqrt( ( (x2 - x1)**2 + (y2 - y1)**2 ) )


def calculate_midpoint(A, B):
    """Calculate the midpoint between two points A and B."""
    x1, y1 = A
    x2, y2 = B
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    return (mid_x, mid_y)


def rotate_2d_points(points, theta=0, axis=None):
    """Rotate or reflect 2D points by theta degrees around the origin or inverting the specified axis."""
    points = np.asarray(points)
    if points.shape[1] != 2:
        raise ValueError("Points should be in shape (n, 2)")
    if axis == 'x':
        # invert the y-coordinates.
        rot_matrix = np.array([
            [1, 0],
            [0, -1]
        ])
    elif axis == 'y':
        # invert the x-coordinates.
        rot_matrix = np.array([
            [-1, 0],
            [0, 1]
        ])
    else:
        # rotation around the origin by theta.
        theta = np.radians(theta)
        rot_matrix = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
    
    return np.dot(points, rot_matrix.T)


def create_flat_image(size=(750, 750), color_mode='RGB', color = 'White',return_ = True, save = False, save_path = None, file_name = None):
        """
        Create an image of the specified size and color mode.
        Parameters:
        size (tuple): The dimensions of the image (width, height).
        color_mode (str): The color mode of the image, either 'RGB' or 'Gray'.
        Returns:
        numpy.ndarray: The created white image.
        """
        col = 255 if color.lower() == 'white' else 0
        
        if color_mode.lower() == 'rgb':
                image = np.ones((size[1], size[0], 3), dtype=np.uint8) * col
        elif color_mode.lower() == 'gray':
                image = np.ones((size[1], size[0]), dtype=np.uint8) * col
        else:
                raise ValueError("Invalid color mode. Choose 'RGB' or 'Gray'.")
        if save:
                path_to_save = save_path_generator(file_name, save_path, flag=f'{size}_{color}')
                plt.imsave(path_to_save, image)
        
        if return_:
                return image
        else:
                return
#end#