'''Program for morphological image operations-
erosion, dilation, opening and closing.'''


import cv2
import numpy as np

# Load the image
image = cv2.imread('Morphologi_of_Img_Operation.jpg', 0)  # Load the image in grayscale

# Define kernel size
kernel = np.ones((5, 5), np.uint8)

# Erosion
erosion = cv2.erode(image, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(image, kernel, iterations=1)

# Opening (Erosion followed by dilation)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Closing (Dilation followed by erosion)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display results
cv2.imshow('Original Image', image)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
