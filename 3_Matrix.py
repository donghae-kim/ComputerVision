import numpy as np
import cv2 as cv

print("\n버전확인")
print('Hello OpenCV', cv.__version__)

print("\n이미지 불러오기")
img = cv.imread('lenna.bmp',flags=cv.IMREAD_REDUCED_COLOR_2)

if img is None:
    print('Image load failed!')
    exit()

cv.imshow('image',img)
cv.waitKey()


print("\nmatrix 연산")
def func1():
    img1 = cv.imread('cat.bmp',cv.IMREAD_GRAYSCALE)
    if img1 is None:
        print('image failed')
        return

    print('type(img1):',type(img1))
    print('img1.shape:',img1.shape)

    if len(img1.shape)==2:
        print('img1 is grayscale')
    elif len(img1.shape)==3:
        print('img1 is a truecolor')

    cv.imshow('img1',img1)
    cv.waitKey()
    cv.destroyAllWindows()

func1()

def func2():
    img1 = np.empty((480,640),np.uint8)
    img2 = np.zeros((480,640,3),np.uint8)
    img3 = np.ones((480,640),np.int32)
    img4 = np.full((480,640),0,np.float32)

    mat1 = np.array([[11,12,13,14],
                     [21,22,23,24],
                     [31,32,33,34]]).astype(np.uint8)

    mat1[0,1]=100
    mat1[2,:]=200

    print(mat1)
func2()

nums = np.array([1,4,2,5,3])
ref = nums[1:4]
cpy = nums[1:4].copy()
print(ref)
print(cpy)
nums[2]=10
print(ref)
print(cpy)

def func3():
    img1 = cv.imread('cat.bmp')
    img2 = img1
    img3 = img1.copy()

    img1[:, :] = (0, 255, 255)
    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)
    cv.waitKey()
    cv.destroyAllWindows()
func3()


def func4():
    img1 = cv.imread('lenna.bmp',cv.IMREAD_GRAYSCALE)
    img2 = img1[200:400,200:400]
    img3 = img1[200:400,200:400].copy()


    #img2 = ~img2
    # img2[:,:]=~img2
    img2[:, :] = 255-img2
    #이거두개차이 ?


    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)
    cv.waitKey()
    cv.destroyAllWindows()

func4()


def func6():
    mat1 = np.ones((3,4),np.int32)
    mat2 = np.arange(12).reshape(3,4)
    mat3 = mat1+mat2
    mat4 = mat2*2

    print("mat1:")
    print(mat1)
    print("mat2:")
    print(mat2)
    print("mat3:")
    print(mat3)
    print("mat4:")
    print(mat4)
func6()