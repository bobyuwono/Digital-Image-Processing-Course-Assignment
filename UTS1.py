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
            b = b/255
            g = g/255
            r = r/255

            #mencari nilai maksimum dan minimum rgb
            minimum = min(b,g,r)
            maximum = max(b,g,r)

            # mencari selisih maximum dan minimum
            delta = maximum - minimum

            #menentukan nilai V
            v = maximum

            #menentukan nilai S
            if (maximum != 0):
                s = delta / maximum
            else:
                s = 0

            #menentukan nilai H
            if (max==min):
                h=0
            elif (r == max):
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
            canvas.itemset((i,j,2), s)
            canvas.itemset((i,j,0), v)

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
            if(g<45):
                canvas.itemset((i, j, 0), image2[i, j][0])
                canvas.itemset((i, j, 1), image2[i, j][1])
                canvas.itemset((i, j, 2), image2[i, j][2])
    return canvas

RGB_SCALE = 255
CMYK_SCALE = 100


def rgb_to_cmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        # black
        return 0, 0, 0, CMYK_SCALE

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / RGB_SCALE
    m = 1 - g / RGB_SCALE
    y = 1 - b / RGB_SCALE

    # extract out k [0, 1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy

    # rescale to the range [0,CMYK_SCALE]
    return c * CMYK_SCALE, m * CMYK_SCALE, y * CMYK_SCALE, k * CMYK_SCALE

image = cv2.imread("tomato_cmyk.tif")
hsvImage = rgb_to_hsv(image)
imageBaru = back_to_rgb( hsvImage , image )
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#
# plt.figure(1)
# plt.imshow(hsvImage ) #.cvtColor(hsvImage, cv2.COLOR_BGR2RGB))
# plt.show()


# cv2.imwrite('hasilakhir.png', imageBaru)
# #show image hasil filtering dan hasil pengembalian value pixel lama
# cv2.imshow("hacu", hsvImage)
cv2.imshow("test", imageBaru)
cv2.waitKey(0)
