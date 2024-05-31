# # analyzer/utils.py
# import cv2
# import os

# def analyze_image_colors(image_path):
#     # Ensure the path is correct
#     absolute_image_path = os.path.join(os.path.dirname(__file__), '..', image_path)
#     print(f"Loading image from: {absolute_image_path}")

#     # Read the image
#     image = cv2.imread(absolute_image_path)

#     if image is None:
#         raise ValueError(f"Image at path {absolute_image_path} could not be loaded.")

#     # Assuming the strip is vertically oriented and each test is equally spaced
#     height, width, _ = image.shape
#     strip_height = height // 10

#     colors = []

#     for i in range(10):
#         # Extract each strip region
#         strip_region = image[i * strip_height:(i + 1) * strip_height, :]
#         # Calculate the mean color of the strip region
#         mean_color = cv2.mean(strip_region)[:3]  # Ignore alpha channel if present
#         # Convert BGR to RGB
#         mean_color_rgb = (int(mean_color[2]), int(mean_color[1]), int(mean_color[0]))
#         colors.append(mean_color_rgb)

#     return colors

import cv2
import numpy as np
from sklearn.cluster import KMeans
import os

def analyze_image_colors(image_path, n_colors=3):
    """
    Analyze the colors on the urine strip image and return a dictionary of RGB values.

    Args:
        image_path (str): The file path to the image.

    Returns:
        dict: A dictionary with labels as keys and RGB values as values.
    """
    absolute_image_path = os.path.join(os.path.dirname(__file__), '..', image_path)
    image = cv2.imread(absolute_image_path)

    if image is None:
        raise ValueError(f"Image at path {absolute_image_path} could not be loaded.")

    # Convert to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    height, width, _ = hsv_image.shape
    strip_height = height // 10

    labels = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
    colors = {}

    for i, label in enumerate(labels):
        strip_region = hsv_image[i * strip_height:(i + 1) * strip_height, :]

        # Flatten the strip region into a 2D array
        pixels = strip_region.reshape(-1, 3)

        # Perform k-means clustering to find the most dominant color
        kmeans = KMeans(n_clusters=1)  # Changed from 3 to 1
        kmeans.fit(pixels)

        # Convert the cluster center back to RGB
        dominant_color = kmeans.cluster_centers_[0]
        dominant_color_rgb = cv2.cvtColor(np.uint8([[dominant_color]]), cv2.COLOR_HSV2RGB)[0][0]

        colors[label] = dominant_color_rgb
    return colors
