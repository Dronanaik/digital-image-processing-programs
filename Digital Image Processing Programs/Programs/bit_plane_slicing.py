'''Program to perform Bit plane slicing'''

import cv2
import numpy as np

def bit_plane_slice(image, bit):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Extract the specified bit-plane
    bit_plane = (gray_image >> bit) & 1
    
    # Scale the bit-plane to 255 to make it visible
    bit_plane *= 255
    
    return bit_plane

# Load an image
image = cv2.imread('Bit_slicing.jpg')

# Set the bit-plane level (0-7 for an 8-bit image)
bit_level = 0

# Perform bit-plane slicing
bit_plane_image = bit_plane_slice(image, bit_level)

# Display the original and bit-plane sliced images
cv2.imshow('Original Image', image)
cv2.imshow(f'Bit-Plane {bit_level}', bit_plane_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
