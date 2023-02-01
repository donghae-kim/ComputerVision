import math
import cv2 as cv


img = cv.imread('Dice1_p5.png')
# img = cv.imread('Dice3_p5.png')
# img = cv.imread('Dice5_p5.png')
# img = cv.imread('img5_1.png')
# img = cv.imread('img5_2.png')
# img = cv.imread('img5_3.png')
# img = cv.imread('img5_4.png')
# img = cv.imread('img5_5.png')
# img = cv.imread('img5_6.png')
# img = cv.imread('img5_7.png')
# img = cv.imread('img5_8.png')
# img = cv.imread('img5_9.png')
# img = cv.imread('img5_10.png')
# img = cv.imread('img5_11.png')

squares = []

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

thresh = cv.threshold(gray_img,170,255, cv.THRESH_BINARY)[1]
kernel = cv.getStructuringElement(cv.MORPH_RECT, (2,2))
close = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
close = cv.morphologyEx(close, cv.MORPH_CLOSE, kernel, iterations=1)
cv.imshow('close',close)

contours, _ = cv.findContours(close, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for cont in contours:

    if cv.contourArea(cont) < 500:
        continue
    count = 0
    approx = cv.approxPolyDP(cont, cv.arcLength(cont, True) * 0.02, True)
    vtc = len(approx)

    if 4 <= vtc :
        (x, y, w, h) = cv.boundingRect(cont)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
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
            if ratio > 0.8:
                cv.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)
                count += 1

        if count != 0:
            squares.append(count)
            count = 0

squares.sort()
print(squares)
cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()