'''Program for Image compression using Block truncation coding.'''
import numpy as np
import cv2
import matplotlib.pyplot as plt

def block_truncation_coding(image, block_size):
    height, width = image.shape
    compressed_image = np.zeros((height, width), dtype=np.uint8)

    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            block = image[i:i+block_size, j:j+block_size]
            threshold = np.mean(block)
            compressed_image[i:i+block_size, j:j+block_size] = (block > threshold) * 255

    return compressed_image

image = cv2.imread("compression.jpg", cv2.IMREAD_GRAYSCALE)

plt.subplot(1,2,1)
plt.title('original image')
plt.imshow(image, cmap='gray')
plt.axis('off')
block_size = 8
compressed_image = block_truncation_coding(image, block_size)
plt.subplot(1,2,2)
plt.title('block truncated image')
plt.imshow(compressed_image, cmap='gray')
plt.axis('off')
plt.show()
