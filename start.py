import cv2 as cv
import numpy as np
FILENAME = "map.jpg"
SIZE = 14

img = cv.imread(FILENAME, cv.IMREAD_GRAYSCALE)
output = np.zeros((len(img), len(img[0])))

font = cv.FONT_HERSHEY_SIMPLEX


# np.random.randint()




lst = []
for i in range(int(round(len(img) / SIZE))):
    for j in range(int(round((len(img[0]) / SIZE)))):
        kernel = img[i * SIZE: (i + 1) * SIZE, j * SIZE: (j + 1)  * SIZE]
        if np.mean(kernel) > np.mean(img):
            cv.putText(output,str(np.random.randint(0, 2)),(j * SIZE, i * SIZE), font, 0.5, (255), 1, cv.LINE_AA)
        # else:
        #     cv.putText(output,'1',(j * SIZE, i * SIZE), font, 0.5, (0), 1, cv.LINE_AA)

    




# kernel = np.ones((28, 28)) / (28 **2) 
# print(kernel)


# print(output)

# new = cv.filter2D(img, cv.IMREAD_GRAYSCALE, kernel)
# print(new)
# print(len(new))
cv.imshow("image", output)
cv.waitKey(0)
cv.destroyAllWindows()


# cv2.imwrite("endproduct.png", img)
