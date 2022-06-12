import cv2 as cv
import numpy as np
from PIL import ImageGrab


upgrade_box = [600, 400, 601, 990]
gray = [14, 16, 24]

img = np.array(ImageGrab.grab(bbox=upgrade_box))

for y in range(len(img)):
    for x in range(len(img[y])):
        if img[y][x][0] == 14:
            print(y,x)

