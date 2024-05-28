'''Program to display an Image as grayscale image,
RED image, GREEN image, BLUE image andalso display
the ID convolution & 2D convolution on an image'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Flower_convolution.jpg')
plt.subplot(2, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.subplot(2, 3, 2)
plt.title('Grayscale Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
b, g, r = cv2.split(image)
plt.subplot(2, 3, 3)
plt.title('Red Channel')
plt.imshow(r, cmap='Reds_r')
plt.axis('off')
plt.subplot(2, 3, 4)
plt.title('Green Channel')
plt.imshow(g, cmap='Greens_r')
plt.axis('off')
plt.subplot(2, 3, 5)
plt.title('Blue Channel')
plt.imshow(b, cmap='Blues_r')
plt.axis('off')
kernel_1d = np.array([1, 0, -1])
conv_1d_image = cv2.filter2D(gray_image, -1, kernel_1d)
plt.subplot(2, 3, 6)
plt.title('1D Convolution')
plt.imshow(conv_1d_image, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()
kernel_2d = np.array([[1, 1, 1],
 [1, -8, 1],
 [1, 1, 1]])
conv_2d_image = cv2.filter2D(gray_image, -1, kernel_2d)
plt.subplot(2, 3, 6)
plt.title('2D Convolution')
plt.imshow(conv_2d_image, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()

