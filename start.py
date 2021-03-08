import cv2 as cv
import numpy as np
import random
FILENAME = "static/images/map.jpg"
path = "static/images/"
WIDTH = 18
HEIGHT = 24

img = cv.imread(FILENAME, cv.IMREAD_GRAYSCALE)
lightO = cv.imread(path+"lightO.jpg", cv.IMREAD_GRAYSCALE)
light1 = cv.imread(path+"light1.jpg", cv.IMREAD_GRAYSCALE)
darkO = cv.imread(path+"darkO.jpg", cv.IMREAD_GRAYSCALE)
dark1 = cv.imread(path+"dark1.jpg", cv.IMREAD_GRAYSCALE)
output = np.zeros((len(img), len(img[0])))


def setImage(img, x, y):
    for i in range(len(img)):
        for j in range(len(img[0])):
            if x + i < len(output) and y + j < len(output[0]):
                output[x + i, y + j] = img[i, j] / 255

    


for i in range(int(round(len(img) / WIDTH))):
    for j in range(int(round((len(img[0]) / HEIGHT)))):
        kernel = img[i * HEIGHT: (i + 1) * HEIGHT,
                     j * HEIGHT: (j + 1) * HEIGHT]
        rand = random.randint(0, 1)
        if np.mean(kernel) > np.mean(img):
            if rand == 1:
                setImage(light1, i * HEIGHT, j * HEIGHT)
            else:
                setImage(lightO, i * HEIGHT, j * HEIGHT)
        else:
            if rand == 1:
                setImage(dark1, i * HEIGHT, j * HEIGHT)
            else:
                setImage(darkO, i * HEIGHT, j * HEIGHT)


cv.imshow("image", output)
cv.waitKey(0)
cv.destroyAllWindows()

print(output)
# cv.imwrite("Mapfinal.jpg", output * 255)
