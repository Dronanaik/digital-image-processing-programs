'''Program for Image watermarking'''

from watermarker.marker import add_mark
import cv2

add_mark(file="Watermarking.jpg", 
         out="watermarked",
         mark="anjchan", 
         size=60,
         color="#ffffff",
         opacity=0.5, 
         angle=30, 
         space=60)
