import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('flowers.tif',0)
img2 = img.copy()
template = cv2.imread('templates.tif',0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['CCOEFF', 'CCOEFF_NORMED', 'CCORR',
            'CCORR_NORMED', 'SQDIFF', 'SQDIFF_NORMED']

for metode in methods:
    img = img2.copy()

    # create method by using custom string
    used_method = 'cv2.TM_' + metode
    method = eval(used_method)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 7)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle('Menggunakan Metode '+ metode)

    plt.show()