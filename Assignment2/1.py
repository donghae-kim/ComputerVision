import cv2 as cv

img = cv.imread('D1.png',cv.IMREAD_GRAYSCALE)
# img = cv.imread('D5.png',cv.IMREAD_GRAYSCALE)
# img = cv.imread('D7.png',cv.IMREAD_GRAYSCALE)
# img = cv.imread('D9.png',cv.IMREAD_GRAYSCALE)

if img is None:
    print('no picture error')
    exit()
blurred = cv.blur(img,(3,3))
circles = cv.HoughCircles(blurred,cv.HOUGH_GRADIENT,1,30,param1=150,param2=30)
circles=circles[0,:]
print(len(circles))

