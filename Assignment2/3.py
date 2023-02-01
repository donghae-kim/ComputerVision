import math
import cv2 as cv

img = cv.imread('WhiteDice.png')
# img = cv.imread('BlackDice.png')

squares = []
if img is None:
    print('no picture error')
    exit()

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray_img = cv.equalizeHist(gray_img)
thresh = cv.threshold(gray_img,220,255, cv.THRESH_BINARY)[1]
kernel = cv.getStructuringElement(cv.MORPH_RECT, (2,2))
close = cv.erode(thresh,kernel)
cv.imshow('a',close)

contours, _ = cv.findContours(close, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
for cont in contours:
    if cv.contourArea(cont) < 50:
        continue
    count = 0
    approx = cv.approxPolyDP(cont, cv.arcLength(cont, True) * 0.02, True)
    vtc = len(approx)

    if 4==vtc :
        (x, y, w, h) = cv.boundingRect(cont)
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        img2 = img[y:y + h, x:x + w]
        cont, ___ = cv.findContours(close[y:y + h, x:x + w], cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
        for cont in cont:
            if cv.contourArea(cont) < 50:
                continue
            approx = cv.approxPolyDP(cont, cv.arcLength(cont, True) * 0.02, True)
            (x, y, w, h) = cv.boundingRect(cont)
            length = cv.arcLength(cont, True)
            area = cv.contourArea(cont)
            ratio = 0
            if length != 0:
                ratio = 4. * math.pi * area / (length * length)
            if ratio > 0.85:
                cv.rectangle(img2, (x, y), (x + w, y + h), (255, 255, 0), 2)
                count+=1
        if count != 0:
            squares.append(count)

squares.sort()
print(squares)

cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()