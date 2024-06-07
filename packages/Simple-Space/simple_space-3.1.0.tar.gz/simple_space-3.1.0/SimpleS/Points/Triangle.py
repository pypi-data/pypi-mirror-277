import matplotlib.pyplot as plt
import numpy as np


def calculate_triangle_perimeter(A, B, C):
    """
    Calculate the perimeter of a triangle given its points.
    Args:
    A, B, C (tuple): Points of triangle. A = (x1, y1), B = (x2, y2), C = (x3, y3)
    Returns:
    float: Perimeter of the triangle.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    # Calculate the lengths of the sides
    a = np.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    b = np.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    c = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return a + b + c



def calculate_triangle_area(A, B, C):
    """
    Calculate the area of a triangle given its points using Heron's formula.
    Args:
    A, B, C (tuple): Points of triangle. A = (x1, y1), B = (x2, y2), C = (x3 , y3)
    Returns:
    float: Area of the triangle.
    """
    # Given Its Points, The sides would be 
    # AB -> we will call it 'c'
    # AC -> 'b' 
    # BC -> 'a' 
    # And we assume P is the around area !
    # S = sqrt( P *(P-a)*(P-b)*(P-c) )
    # P = 1/2 ( a + b + c )
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    a = np.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    b = np.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    c = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    s = (a + b + c) / 2
    return np.sqrt(s * (s - a) * (s - b) * (s - c))


def calculate_triangle_shoelace_area(P1, P2, P3):
    """
    Calculate the area of a triangle given its vertices using the shoelace formula.
    Args:
    P1, P2, P3 (tuple): Vertices of the triangle.
    Returns:
    float: Area of the triangle.
    """
    return 0.5 * abs(P1[0]*P2[1] + P2[0]*P3[1] + P3[0]*P1[1] - P1[1]*P2[0] - P2[1]*P3[0] - P3[1]*P1[0])


def plot_filled_triangle_by_amount(A, B, C, amount):
    """
    Plots an original triangle defined by three vertices (A, B, C) and fills amount within it!
    Parameters:
    A (tuple): A tuple (x1, y1) representing the coordinates of the first vertex of the triangle.
    B (tuple): A tuple (x2, y2) representing the coordinates of the second vertex of the triangle.
    C (tuple): A tuple (x3, y3) representing the coordinates of the third vertex of the triangle.
    amount (float): The desired area of the smaller, proportionally scaled triangle to be filled within the original triangle.
    Returns:
    None: This function plots the original triangle and the filled amount inside it! but does not return any values.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    total_area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)
    desired_area = amount
    #assume it's scaled proportionally
    scaling_factor = (desired_area / total_area) ** 0.5
    # Calculate the new vertices
    x_fill1, y_fill1 = x1, y1
    x_fill2, y_fill2 = x1 + scaling_factor * (x2 - x1), y1 + scaling_factor * (y2 - y1)
    x_fill3, y_fill3 = x1 + scaling_factor * (x3 - x1), y1 + scaling_factor * (y3 - y1)
    plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'k-')
    plt.fill([x_fill1, x_fill2, x_fill3, x_fill1], [y_fill1, y_fill2, y_fill3, y_fill1], 'blue', alpha=0.5)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Triangle with Specific Area Filled')
    plt.grid(True)
    plt.show()


def edge_lengths(pts):
    """
    Compute the edge lengths of a triangle given its vertices
    """
    return np.linalg.norm(pts[1] - pts[0]), np.linalg.norm(pts[2] - pts[1]), np.linalg.norm(pts[0] - pts[2])


def circumcircle_radius(pts):
    """
    Compute the circumcircle radius of a triangle given its vertices
    """
    a, b, c = edge_lengths(pts)
    area = calculate_triangle_shoelace_area(pts)
    return (a * b * c) / (4 * area)



def is_point_in_triangle(P, P1, P2, P3):
    
    """
    Determine if a point P is inside the triangle formed by points P1, P2, and P3.
    Args:
    P (tuple): Coordinates of the point to check.
    P1, P2, P3 (tuple): Vertices of the triangle.
    Returns:
    bool: True if the point is inside the triangle, False otherwise.
    """
    # area of main triangle
    area_main = calculate_triangle_area(P1, P2, P3)
    # areas of the triangles formed with the point and each pair of vertices
    area1 = calculate_triangle_area(P, P1, P2)
    area2 = calculate_triangle_area(P, P2, P3)
    area3 = calculate_triangle_area(P, P3, P1)
    # the sum of the areas equals the area of the main triangle ?
    
    return abs(area_main - (area1 + area2 + area3)) < 1e-9 


def chech_points_pos_vs_triangle(P1, P2, P3, test_point, use_lim = True , x_lim=(-10, 10), y_lim=(-10, 10),
                                 triangle_label = 'Triangle', triangle_edgecolor = 'blue',
                                 points_label = 'Triangle Vertices',points_color = 'yellow',
                                 test_point_label = 'Test Point', test_point_color = 'black',
                                 inside_color = 'green', inside_label ='Inside',
                                 outside_color= 'red' , outside_label =  'Outside',
                                 plot_title = ' Test Point  VS  Triangle '):
    """
    optionally check if a test point lies within the triangle formed by these points.
    Args:
    P1 (tuple): Coordinates of the first point (i1, j1).
    P2 (tuple): Coordinates of the second point (i2, j2).
    P3 (tuple): Coordinates of the third point (i3, j3).
    test_point (tuple, optional): The point to test whether it lies within the triangle.
    xlim (tuple): Limits for the x-axis as (xmin, xmax).
    ylim (tuple): Limits for the y-axis as (ymin, ymax).
    Returns:
    bool: True if the test point is inside the triangle, False otherwise.
    """
    points = [P1, P2, P3]
    fig, ax = plt.subplots()
    x_coords, y_coords = zip(*points)
    if use_lim and x_lim is not None :
        ax.set_xlim(x_lim)
    if use_lim and y_lim is not None :
        ax.set_ylim(y_lim)
    ax.scatter(x_coords, y_coords, color=points_color, label=points_label)
    # triangle formed by the points
    triangle = plt.Polygon(points, fill=None, edgecolor=triangle_edgecolor, linestyle='--', label=triangle_label)
    ax.add_patch(triangle)
    result = None
    if test_point:
        ax.scatter(*test_point, color = test_point_color, label=test_point_label)
        result = is_point_in_triangle(test_point, P1, P2, P3)
        if result:
            plt.text(test_point[0], test_point[1], inside_label, fontsize=12, color=inside_color)
        else:
            plt.text(test_point[0], test_point[1],outside_label, fontsize=12, color=outside_color)
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(plot_title)
    ax.legend()
    plt.show()
    return result


def create_triangle_with_points(P1, P2, P3, xlim=(-10, 10), ylim=(-10, 10)):
    
    """
    Create and display a Euclidean plane with three given points P1, P2, and P3.
    Args:
    P1 (tuple): Coordinates of the first point (i1, j1).
    P2 (tuple): Coordinates of the second point (i2, j2).
    P3 (tuple): Coordinates of the third point (i3, j3).
    xlim (tuple): Limits for the x-axis as (xmin, xmax).
    ylim (tuple): Limits for the y-axis as (ymin, ymax).
    """
    points = [P1, P2, P3]
    fig, ax = plt.subplots()
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    x_coords, y_coords = zip(*points)
    ax.scatter(x_coords, y_coords, color='red', label='Points')
    triangle = plt.Polygon(points, fill=None, edgecolor='blue', linestyle='--', label='Triangle')
    ax.add_patch(triangle)
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Euclidean Plane with Points P1, P2, P3')
    ax.legend()
    plt.show()
    return triangle


def plot_delaunay_triangle(points, delaunay, ax=None):
    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = None
    for simplex in delaunay.simplices:
        ax.plot(points[simplex, 0], points[simplex, 1], 'k-')
    if fig is not None:
        return fig, ax


class SeveralTriangles:
    
    def __init__(self):
        self.triangles = []
    
    def add_triangle(self, triangle):
        """
        Adds a single triangle or a list of triangles to the list of triangles.
        Parameters:
        triangle: A single tuple representing the vertices of a triangle, 
                  or a list of such tuples.
        Returns:
        None
        """
        if isinstance(triangle, tuple):
            self.triangles.append(triangle)
        elif isinstance(triangle, list) and isinstance(triangle[0], tuple):
            self.triangles.extend(triangle)
        else:
            raise TypeError("This method expects triangles as tuples of vertex coordinates or a list of such tuples.")
    
    def plot_triangles(self, 
                        triangle_index:int = None, 
                        amount:float = None,
                        just_draw_the_specified_index = False):
        """
        Plots a triangle from the list of triangles and fills a smaller triangle within it,
        scaled to a specified area.
        Parameters:
        triangle_index (int): Index of the triangle in the list of triangles.
        amount (float): The desired area of the smaller, proportionally scaled triangle to be filled within the original triangle.
        Returns:
        None: This function plots the original triangle and the filled smaller triangle but does not return any values.
        """
        if amount is None :
            if triangle_index is None :
                for any_ in self.triangles:
                    x1, y1 = any_[0]
                    x2, y2 = any_[1]
                    x3, y3 = any_[2]
                    plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'k-')
            elif triangle_index is not None :
                triangle = self.triangles[triangle_index]
                A, B, C = triangle
                x1, y1 = A
                x2, y2 = B
                x3, y3 = C
                plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'k-')
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.title('Triangle with Specific Area Filled')
            plt.grid(True)
            plt.show()
            return
        else:
            pass
        if not (0 <= triangle_index < len(self.triangles)):
            raise ValueError("Invalid triangle index. Please provide a valid index.")
        triangle = self.triangles[triangle_index]
        A, B, C = triangle
        x1, y1 = A
        x2, y2 = B
        x3, y3 = C
        total_area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
        scaling_factor = (amount / total_area) ** 0.5
        x_fill1, y_fill1 = x1, y1
        x_fill2, y_fill2 = x1 + scaling_factor * (x2 - x1), y1 + scaling_factor * (y2 - y1)
        x_fill3, y_fill3 = x1 + scaling_factor * (x3 - x1), y1 + scaling_factor * (y3 - y1)
        plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'k-')
        plt.fill([x_fill1, x_fill2, x_fill3, x_fill1], [y_fill1, y_fill2, y_fill3, y_fill1], 'blue', alpha=0.5)
        if not just_draw_the_specified_index:
            temp_list = self.triangles.copy()
            temp_list.pop(triangle_index)
            for any_ in temp_list:
                x1, y1 = any_[0]
                x2, y2 = any_[1]
                x3, y3 = any_[2]
                plt.plot([x1, x2, x3, x1], [y1, y2, y3, y1], 'k-')
        else:
            pass
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Triangle with Specific Area Filled')
        plt.grid(True)
        plt.show()
    
#end