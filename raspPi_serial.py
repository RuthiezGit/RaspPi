import Rpi.GPIO as gpio
import serial
import time


#initalize or open the serial port
py_ser = serial.Serial("COM15", 9600, timeout = 1)
while True:
    # x = py_ser.read() #with empty argument
    # s = py_ser.read(10) #with an existing or filled argument but takes only one byte, i.e 1, 2, 3,4 etc
    # line = py_ser.readline() #to read a line of argument
      
    command = input("")
    py_ser.write(str.encode(command))
    time.sleep(0.5)

    line = py_ser.readline()
    print(line)

