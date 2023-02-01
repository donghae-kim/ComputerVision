import cv2 as cv
import numpy as np

def func1():
    img1 = cv.imread('sample.jpg', cv.IMREAD_GRAYSCALE)
    mean_img = np.mean(img1, dtype=np.int32)
    height, width = img1.shape

    for i in range(height):
        for j in range(width):
            if img1[i][j] < mean_img:
                img1[i][j] = 0

    cv.imshow('img1', img1)
    cv.waitKey()
    cv.destroyAllWindows()
    cv.imwrite("output.jpg",img1)

func1()