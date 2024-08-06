'''Program to perform the basic arithmetic and logical operations on the images.'''


import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load two images
img1 = cv2.imread('Lion_Arth_Logi.jpg')
img2 = cv2.imread('Falls_Arth_Logi.jpg')

# Check if the images were loaded properly
if img1 is None or img2 is None:
    raise ValueError("One of the images didn't load correctly")

# Resize the second image to match the dimensions of the first image
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Perform arithmetic operations
add = cv2.add(img1, img2_resized)
subtract = cv2.subtract(img1, img2_resized)
multiply = cv2.multiply(img1, img2_resized)
divide = cv2.divide(img1, img2_resized)

# Perform logical operations
bitwise_and = cv2.bitwise_and(img1, img2_resized)
bitwise_or = cv2.bitwise_or(img1, img2_resized)
bitwise_xor = cv2.bitwise_xor(img1, img2_resized)
bitwise_not_img1 = cv2.bitwise_not(img1)
bitwise_not_img2 = cv2.bitwise_not(img2_resized)

# Display results
titles = ['Original img1', 'Original img2', 'Addition', 'Subtraction', 'Multiplication', 'Division',
          'Bitwise AND', 'Bitwise OR', 'Bitwise XOR', 'Bitwise NOT (Image 1)', 'Bitwise NOT (Image 2)']
images = [img1, img2, add, subtract, multiply, divide,
          bitwise_and, bitwise_or, bitwise_xor, bitwise_not_img1, bitwise_not_img2]

plt.figure(figsize=(12, 9))  # Adjust the figure size as needed

for i in range(len(images)):
    plt.subplot(3, 4, i+1)  # Create a 3x4 grid for subplots
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()



