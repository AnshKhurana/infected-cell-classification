import cv2
from matplotlib import pyplot as plt
import numpy as np


im = cv2.imread("test.png")
print(type(im))

print(im.shape)
print(type(im[0]))

plt.imshow(im)
plt.show()