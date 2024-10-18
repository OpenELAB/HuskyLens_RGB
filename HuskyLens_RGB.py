import RPi.GPIO as GPIO
import math
import serial
import sys
from time import sleep
import time
import threading

GPIO.setmode(GPIO.BCM)
LedPinR = 17
GPIO.setup(LedPinR, GPIO.OUT)
LedPinG = 27
GPIO.setup(LedPinG, GPIO.OUT)
LedPinB = 22
GPIO.setup(LedPinB, GPIO.OUT)
R = GPIO.PWM(LedPinR, 2000)
G = GPIO.PWM(LedPinG, 1999)
B = GPIO.PWM(LedPinB, 5000)
R.start(0)
G.start(0)
B.start(0)
ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=2)
ID = 30
Number = 8
color_number = 0
x = 0
yes_no = 0
print("serial test start ...")
data_position = 0
Current_color = 0
over = 1
code = 0
i = 7.5

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col):
    R_val = (col & 0xff0000) >> 16
    G_val = (col & 0x00ff00) >> 8
    B_val = (col & 0x0000ff) >> 0

    R_val = map(R_val, 0, 255, 0, 100)
    G_val = map(G_val, 0, 255, 0, 100)
    B_val = map(B_val, 0, 255, 0, 100)

    R.ChangeDutyCycle(R_val)
    G.ChangeDutyCycle(G_val)
    B.ChangeDutyCycle(B_val)


while True:
    data_all = []
    i = 0
    while ser.inWaiting() > 0:
        str_n = ser.read()
        str_y = str(str_n.hex())
        if data_position == 0 and str_y != '55':
            continue
        ser.write(str_n)
        data_all.append(str_y)
        data_position += 1
        i += 1
        if data_position == 6:
            try:
                x = int(str_y[0]) * 10 + int(str_y[1])
            except:
                print("data error1")
            if x > 0:
                yes_no = x
                print("This time %d individuals were color" % yes_no)
            else:
                yes_no = 0
                print("No color was recognized.")
        if (data_position == 16 and yes_no == 0) or (data_position == 31 + (yes_no - 1) * 16 and yes_no != 0):
            break
    if yes_no > 0:
        for i in range(0, 16 + yes_no * 16 - 1, 1):
            if i == Number - 1:
                try:
                    x = int(data_all[i][0]) * 10 + int(data_all[i][1])
                except:
                    print("data error2")
                color_number = x
                print("Currently %d color data has been saved." % x)
            if i == ID + Current_color * 16 - 1:
                try:
                    x = int(data_all[i][0]) * 10 + int(data_all[i][1])
                except:
                    print("data error3")
                    print("Identify the color with ID %d" % x)
                Current_color += 1
                match x:
                    case 1:
                        print("color is red")
                        setColor(0x00ff00)
                    case 2:
                        print("color is green")
                        setColor(0xff0000)
                    case 3:
                        print("color is orange")
                        setColor(0xff9300)
                    case 4:
                        print("color is blue")
                        setColor(0x0000ff)
                    case 5:
                        print("color is yellow")
                        setColor(0xfffb00)

    sleep(0.1)
    data_position = 0
    Current_color = 0
    yes_no = 0
    ser.write([0x55, 0xaa, 0x11, 0x00, 0x24, 0x34])
    print('send')

