import cv2
import numpy as np
from matplotlib import pyplot as plt


#draw line on image
img = cv2.imread('/Users/apple/Desktop/a.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()
cv2.imwrite('watchgray.png',img)

