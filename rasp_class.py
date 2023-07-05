import Rpi.GPIO as gpio
import time
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17,gpio.OUT)
    gpio.setup(22,gpio.OUT)
    gpio.setup(23,gpio.OUT)
    gpio.setup(24,gpio.OUT)

def forward(sec):
    init()
    gpio.output(17,False)
    gpio.output(22,True)
    gpio.output(23,True)
    gpio.output(24,False)
    time.sleep(sec)
    gpio.cleanup()

def backward(sec):
    init()
    gpio.output(17,True)
    gpio.output(22,False)
    gpio.output(23,False)
    gpio.output(24,True)
    time.sleep(sec)
    gpio.cleanup()

def brake():
    init()
    gpio.output(17,False)
    gpio.output(22,False)
    gpio.output(23,False)
    gpio.output(24,False)
    gpio.cleanup()

while True:
    command = input("Your wish is my command: ")
    Time = int (input("in secs: "))
    if command == "f":
        forward(Time)
    elif command == "b":
        backward(Time)
    else:
        brake()


