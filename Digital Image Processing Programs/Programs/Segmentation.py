'''Program for Image segmentation.'''

import cv2
import numpy as np
import matplotlib.pyplot as plt


def edge_based_segmentation(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, 100, 200)
    
    # Find contours in the edge image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create a mask for the segmented regions
    segmented_image = np.zeros_like(gray_image)
    
    # Draw contours on the mask
    cv2.drawContours(segmented_image, contours, -1, (255), thickness=cv2.FILLED)
    
    return segmented_image

# Read the image
image = cv2.imread('Segmentation.jpg')

# Perform edge-based segmentation
segmented_image = edge_based_segmentation(image)

# Display the original and segmented images

plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title('edge based segmented image')
plt.imshow(segmented_image, cmap='gray')
plt.axis('off')
plt.show()
