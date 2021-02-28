import cv2 as cv
import numpy as np
import random
FILENAME = "map2.jpg"
WIDTH = 18
HEIGHT = 24

img = cv.imread(FILENAME, cv.IMREAD_GRAYSCALE)
lightO = cv.imread("lightO.jpg", cv.IMREAD_GRAYSCALE)
light1 = cv.imread("light1.jpg", cv.IMREAD_GRAYSCALE)
darkO = cv.imread("darkO.jpg", cv.IMREAD_GRAYSCALE)
dark1 = cv.imread("dark1.jpg", cv.IMREAD_GRAYSCALE)
output = np.zeros((len(img), len(img[0])))


def setImage(img, x, y):
    letter = cv.imread(img, cv.IMREAD_GRAYSCALE)
    for i in range(len(letter)):
        for j in range(len(letter[0])):
            if x + i < len(output) and y + j < len(output[0]):
                output[x + i, y + j] = letter[i, j] / 255
    


# lst = []
for i in range(int(round(len(img) / WIDTH))):
    for j in range(int(round((len(img[0]) / HEIGHT)))):
        kernel = img[i * WIDTH: (i + 1) * WIDTH, j * HEIGHT: (j + 1) * HEIGHT]
        if np.mean(kernel) > np.mean(img) + 5:
            setImage("dark1.jpg", i * WIDTH, j * HEIGHT)
        else:
            setImage("light1.jpg", i * WIDTH, j * HEIGHT)
        # setImage("light1.jpg", i * HEIGHT, j * HEIGHT)


cv.imshow("image", output)
cv.waitKey(0)
cv.destroyAllWindows()


# cv2.imwrite("endproduct.png", output)
