import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


#draw line on image
img = cv.imread('/Users/apple/Desktop/a.jpg',cv.IMREAD_GRAYSCALE)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()
cv.imwrite('watchgray.png',img)


#load colored image

image=cv.imread('/Users/apple/Desktop/a.jpg', cv.IMREAD_COLOR)#Load the image

cv.imshow('image', image) #Show the image
k = cv.waitKey(0)
