import cv2
# import Rpi.GPIO as gpio
import serial
# import time

py_ser = serial.Serial("COM18", 9600, timeout = 1)
cascade=cv2.CascadeClassifier(r'C:\Users\USER\Downloads\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')

cv2.namedWindow("preview")
web_cam = cv2.VideoCapture(0)

while web_cam.isOpened():
    rval, frame =web_cam.read()
    width, height, ch = frame.shape
    center_frame = (width/2), (height/2)
    if rval:
        faces = cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

        if len(faces)>0:
            x,y,w,h=faces[0]
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h), color=(255,0,0), thickness=1)

            center_obj = ((x+w)/2), ((y+h)/2)
            area_obj = ((x+w)*(y+h))
            area_desired = (width-250)*(height-250)

            a,b = center_frame
            c,d = center_obj
            if (c < (a-20)):
                # print("L")
                py_ser.write(str.encode("L"))
            elif (c > (a+20)):
                # print("R")
                py_ser.write(str.encode("R"))
            
            if (area_obj > area_desired):
                # print("B")
                py_ser.write(str.encode("B"))
            elif (area_obj < area_desired):
                # print("F")
                py_ser.write(str.encode("F"))

            line = py_ser.readline()
            print(line)

        cv2.imshow('preview', frame)
        key =cv2.waitKey(2)
        if key =="q":
            break

# web_cam.release()
# cv2.destroyAllWindows("preview")



