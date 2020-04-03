import numpy
import cv2
import matplotlib.pyplot as plt

def rgb_to_hsv(imagesMtx):
    shape = imagesMtx.shape
    canvas = numpy.zeros((shape[0], shape[1], 3), numpy.uint8)
    for i in range(shape[0]):
       for j in range(shape[1]):
            b, g, r = imagesMtx[i, j]

            #mengubah value rgb agar range nilainya berkurang dari 0-255 menjadi 0-1
            b = b/255.0
            g = g/255.0
            r = r/255.0

            #mencari nilai maksimum dan minimum rgb
            minimum = min(b,g,r)
            maximum = max(b,g,r)

            #menentukan nilai V
            v = maximum

            #mencari selisih maximum dan minimum
            delta = maximum - minimum

            #menentukan nilai S
            if (maximum != 0):
                s = delta / maximum
            else:
                s = 0

            #menentukan nilai H
            if (r == max):
                h = (g - b) / delta
            elif (g == max):
                h = 2 + (b - r) / delta
            else:
                h = 4 + (r - g) / delta
            h *= 60

            #membulatkan nilai h menjadi integer
            if numpy.isnan(h):
                h = numpy.nan_to_num(h)

            #set nilai hsv ke dalam canvas
            canvas.itemset((i,j,1), h)
            canvas.itemset((i,j,0), s)
            canvas.itemset((i,j,2), v)

    #return canvas keluar fungsi
    return canvas

#image1 adalah image orisinil, dan image2 adalah 'image biru'
def back_to_rgb(image1, image2):
    shape = image.shape
    canvas = numpy.zeros((shape[0], shape[1], 3), numpy.uint8)
    for i in  range (shape[0]):
        for j in range(shape[1]):

            b,g,r = image1[i,j]

            #kondisional threshold
            if(b<50):
                canvas.itemset((i, j, 0), image2[i, j][0])
                canvas.itemset((i, j, 1), image2[i, j][1])
                canvas.itemset((i, j, 2), image2[i, j][2])
    return canvas

image = cv2.imread("tomato.jpg")
hsvImage = rgb_to_hsv(image)
imageBaru = back_to_rgb( hsvImage , image )

plt.figure(1)
plt.imshow(cv2.cvtColor(hsvImage, cv2.COLOR_BGR2RGB))
plt.show()

# cv2.imwrite('hasilakhir.png', imageBaru)

# #show image hasil filtering dan hasil pengembalian value pixel lama
# cv2.imshow("hacu", hsvImage)
# cv2.imshow("test", imageBaru)
#
# cv2.waitKey(0)
