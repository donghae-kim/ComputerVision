import cv2 as cv

img = cv.imread('Dices.png',cv.IMREAD_GRAYSCALE)

if img is None:
    print('no picture error')
    exit()

squares = []

ret, thr = cv.threshold(img, 127, 255, cv.THRESH_OTSU)
contours, _ = cv.findContours(thr, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
for cont in contours:
    approx = cv.approxPolyDP(cont, cv.arcLength(cont, True) * 0.02, True)
    vtc = len(approx)
    blurred = cv.blur(img[approx[0][0][1]:approx[2][0][1],approx[0][0][0]:approx[2][0][0]], (3, 3))
    circles = cv.HoughCircles(blurred, cv.HOUGH_GRADIENT, 1, 30, param1=150, param2=30)
    circles = circles[0, :]
    squares.append(len(circles))

squares.sort()
print(squares)
