from svgpathtools import svg2paths
from svgpath2mpl import parse_path
import matplotlib as mpl
from matplotlib.path import Path
from matplotlib.markers import MarkerStyle
import matplotlib.pyplot as plt
import os
import glob
import numpy as np



def get_custom_markers():
    '''A custom matplotlib marker generator.

    This function loads all svg files in a sub-folder named 'support_data' and creates a dictionary of custom matplotlib
    markers.  To use a marker:

    plt.plot(1,1,ls='', marker=custom_markers[aperture_name],  markerfacecolor='k', markeredgecolor='k', markersize=30)

    Parameters
    ----------
    custom_markers : dict
        A dictionary containing the markers for each of the apertures with an svg file in the subdirectory.
    '''

    support_data_path = os.path.join(os.path.dirname(__file__), 'support_data')
    aperture_paths = glob.glob(os.path.join(support_data_path, '*.svg'))

    custom_markers = {}

    for aperture_path in aperture_paths:
        # Get name of aperture
        # Split path
        parts = aperture_path.split('\\')
        file_name = parts[-1]
        
        # Extract the name of the aperture excluding whatever comes after the last underscore
        aperture_name = '_'.join(file_name.split('_')[0:-1])

        loaded_svg, attributes = svg2paths(aperture_path)

        custom_marker = parse_path(attributes[0]['d'])
        custom_marker.vertices -= custom_marker.vertices.mean(axis=0)
        custom_marker = custom_marker.transformed(mpl.transforms.Affine2D().rotate_deg(180))
        custom_marker = custom_marker.transformed(mpl.transforms.Affine2D().scale(-1, 1))

        custom_markers[aperture_name] = custom_marker

    custom_markers['habex'] = get_monolithic_marker()

    return custom_markers


def get_monolithic_marker():
    # Generate marker for monolithic aperture
    
    
    # Define the vertices and codes for the square, shifted so the center is at (0, 0)
    verts_square = [
        (-0.5, -0.5),  # left, bottom
        (-0.5, 0.5),  # left, top
        (0.5, 0.5),  # right, top
        (0.5, -0.5),  # right, bottom
        (-0.5, -0.5),  # back to left, bottom
    ]

    codes_square = [
        Path.MOVETO,  # begin drawing
        Path.LINETO,  # straight line
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY,  # close shape
    ]

    # Define the vertices and codes for the circle (approximation using a polygon)
    num_circle_points = 100
    theta = np.linspace(0, 2 * np.pi, num_circle_points, endpoint=False)
    verts_circle = [(0.45 * np.cos(t), 0.45 * np.sin(t)) for t in theta]
    codes_circle = [Path.MOVETO] + [Path.LINETO] * (num_circle_points - 1) + [Path.CLOSEPOLY]

    # Correct the length of codes_circle to match verts_circle
    verts_circle.append(verts_circle[0])

    # Define the path for the circle
    path_circle = Path(verts_circle, codes_circle)

    # Combine the square and circle into one path
    verts_combined = verts_square + verts_circle
    codes_combined = codes_square + codes_circle

    path_combined = Path(verts_combined, codes_combined)

    # Create a custom marker
    marker = MarkerStyle(marker=path_combined)

    return marker
