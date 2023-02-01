import cv2 as cv
import numpy as np

def saturated(value):
    if value > 255:
        value=255
    elif value<0:
        value=0
    return value

def func2():
    img2 = cv.imread('sample.jpg', cv.IMREAD_GRAYSCALE)
    mean_img = np.mean(img2)
    height, width = img2.shape

    for i in range(height):
        for j in range(width):
            img2[i][j] = saturated(img2[i][j]+(img2[i][j]-mean_img)*2.0)

    cv.imshow('img2', img2)
    cv.waitKey()
    cv.destroyAllWindows()
    cv.imwrite("contrast.jpg", img2)

func2()