'''Program for smoothing an image using low pass filter
and high pass filter in frequency domain'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

def fft_convolve(img,kernel):
    f=np.fft.fft2(img)
    fshift=np.fft.fftshift(f)
    fshift_filtered=fshift*kernel
    f_ishift=np.fft.ifftshift(fshift_filtered)
    img_back=np.fft.ifft2(f_ishift)
    img_back=np.abs(img_back)
    return img_back

img=cv2.imread('Frequency_Domain.jpg',0)
rows,cols=img.shape
mask_lp=np.zeros((rows,cols),np.uint8)
center=(rows//2,cols//2)
radius=30
cv2.circle(mask_lp,center,radius,1,-1)
mask_hp=np.ones((rows,cols),np.uint8)
cv2.circle(mask_hp,center,radius,0,-1)
smoothed_img_lp=fft_convolve(img,mask_lp)
smoothed_img_hp=fft_convolve(img,mask_hp)
plt.figure(figsize=(12,6))
plt.subplot(131),plt.imshow(img,cmap='gray'),plt.title('original image')
plt.subplot(133),plt.imshow(smoothed_img_lp,cmap='gray'),plt.title('high-pass filter')
plt.subplot(132),plt.imshow(smoothed_img_hp,cmap='gray'),plt.title('low-pass filter')
plt.show()
