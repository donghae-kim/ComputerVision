import cv2 as cv
import numpy as np

def func3():
    webcam = cv.VideoCapture(0)
    check = False
    prev_img=0
    gray_flag=False
    time =0;
    time_flag = False

    w=round(webcam.get(cv.CAP_PROP_FRAME_WIDTH))
    h=round(webcam.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = webcam.get(cv.CAP_PROP_FPS)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, fps, (w, h),0)

    while webcam.isOpened():
        status, frame = webcam.read()
        mean_img = np.mean(frame, dtype=np.int32)
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        later_time = int(webcam.get(cv.CAP_PROP_POS_MSEC))



        if gray_flag==True :
            gray_frame = ~gray_frame
            if time_flag==False:
                time = int(webcam.get(cv.CAP_PROP_POS_MSEC))
                time_flag=True



        if (later_time-time)>3000 and time!=0:
            gray_flag=False
            gray_frame = ~gray_frame
            time = 0
            time_flag = False


        if check==False:
            prev_img=mean_img

        if abs(prev_img-mean_img) > 30:
            gray_flag = True

        prev_img = mean_img
        check=True


        if status:
            cv.imshow("gray_frame", gray_frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        out.write(gray_frame)

    webcam.release()
    cv.destroyAllWindows()

func3()