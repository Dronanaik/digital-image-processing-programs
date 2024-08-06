'''Program to sharpen an image using 2-D
Laplacian high pass filter in spatial domain.'''

import cv2
import numpy as np

def sharpen_image(image):
    # Define Laplacian filter
    laplacian_filter = np.array([[0, 1, 0],
                                 [1, -4, 1],
                                 [0, 1, 0]])
   
    # Apply the Laplacian filter to the image
    sharpened_image = cv2.filter2D(image, -1, laplacian_filter)
   
    # Add the filtered result back to the original image to sharpen it
    sharpened_image = cv2.addWeighted(image, 1.0, sharpened_image, -0.5, 0)
   
    return sharpened_image

# Load an image
image_path = 'Sharpning_of_Image.jpg'  # Replace 'your_image_path.jpg' with the path to your image
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found.")
else:
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    # Sharpen the grayscale image
    sharpened_image = sharpen_image(grayscale_image)
   
    # Display the original and sharpened images
    cv2.imshow('Original Image', grayscale_image)
    cv2.imshow('Sharpened Image', sharpened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
