import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('IPB.jpg',0)
cv2.imshow("ipb asli", img)
#Gaussian blur 5x5 and 7x7
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur5 = cv2.GaussianBlur(img,(5,5),0)
blur7 = cv2.GaussianBlur(img,(7,7),0)

cv2.imshow("blur 5 ", blur5)
#image gradient
laplacian = cv2.Laplacian(blur5,cv2.CV_64F)
laplacian2 = cv2.Laplacian(blur7,cv2.CV_64F)
sobelx = cv2.Sobel(blur5,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(blur7,cv2.CV_64F,0,1,ksize=5)

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
magnitude = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
magnitude *= 255.0 / magnitude.max()

angle = np.arctan2(sobel_y, sobel_x)

#non maximum surpression
def non_max_suppression(img, D):
    M, N = img.shape
    Z = np.zeros((M, N), dtype=np.int32)
    angle = D * 180. / np.pi
    angle[angle < 0] += 180

    for i in range(1, M - 1):
        for j in range(1, N - 1):
            try:
                q = 255
                r = 255

                # angle 0
                if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                    q = img[i, j + 1]
                    r = img[i, j - 1]
                # angle 45
                elif (22.5 <= angle[i, j] < 67.5):
                    q = img[i + 1, j - 1]
                    r = img[i - 1, j + 1]
                # angle 90
                elif (67.5 <= angle[i, j] < 112.5):
                    q = img[i + 1, j]
                    r = img[i - 1, j]
                # angle 135
                elif (112.5 <= angle[i, j] < 157.5):
                    q = img[i - 1, j - 1]
                    r = img[i + 1, j + 1]

                if (img[i, j] >= q) and (img[i, j] >= r):
                    Z[i, j] = img[i, j]
                else:
                    Z[i, j] = 0

            except IndexError as e:
                pass

    return Z

# surpression= non_max_suppression(img, 45.0)

cv2.imshow("gambur x",laplacian)
cv2.imshow("gambur y",laplacian2)
# cv2.imshow("surpres 4",surpression)


cv2.imshow("gambar y",magnitude)

cv2.waitKey(0)


##specify imafe path
#image_path = r'C:\Users\Rajnish\Desktop\GeeksforGeeks\geeks.png'

#ini untuk membandingkan dua gambar
plt.subplot(121),plt.imshow(sobel_x),plt.title('sobel x')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(sobel_y),plt.title('sobel y')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude),plt.title('magnitude')
plt.xticks([]), plt.yticks([])
plt.show()