  __Hello__ 👋,Welcome to this tutorial on HuskyLens color recognition! In this project, you will learn how to recognize and track multiple colors using HuskyLens and output the corresponding RGB values. In the following steps 📜, you'll explore step-by-step instructions on how to set up the device, write the code, and successfully get the project up and running. Ready to begin? Let’s dive in 🚀!

- 📝 Project Description
- ✨ Functional characteristics
- 🏗  Project structure
- 🚀 Installation and Operation
- 🔧 Instructions for use

# 颜色识别进行RGB输出项目
## 项目描述
This project implements color recognition using HuskyLens. By learning, recognizing, and tracking multiple colors, the user can obtain the RGB values of the colors in real time and automatically count the color blocks. Ambient light has a significant impact on color recognition, so it is recommended to use this feature in a well-lit environment.
- Learn and track colors: HuskyLens recognizes and tracks colors learned by the user and supports multi-color recognition.
- Automatic counting: When multiple blocks of the same color appear, they can be identified and counted at the same time.
- RGB Output: Implement the change of RGB LED light color through code to show the recognized color in real time.
## 功能特性
- 📏 Accurate Recognition: HuskyLens can accurately recognize and track target colors for a wide range of color scenes.
- 🎉 Highly interactive: users can adjust learning objectives in real time and get color IDs and RGB values through HuskyLens.
- 🔋 Low power consumption: low power consumption of the device, suitable for long time color recognition and tracking.
## 项目结构
```
│── README.md               # 项目说明文件
│── ColorRecognition        # 源代码文件夹
  │── main.py               # 主代码文件
  │── RGBControl.py         # RGB控制代码
  │── HuskyLens.py          # HuskyLens接口代码
```
## 所需材料
1、HuskyLens Color Recognition Sensor  
2、Raspberry Pi (for control)  
3、RGB LED Lights  
4、DuPont wire  
5、Breadboard  
## 接线图与引脚介绍
### HuskyLens 引脚
- Vcc (Power Positive): connected to the 5V pin of the controller.
- GND (Ground): connected to the GND pin of the controller.  
- SDA/SCL (I2C communication): connected to the I2C pins of the controller.  
### RGB LED 引脚
- R (Red): connected to the PWM output pin of the controller.  
- G (green): connected to the PWM output pin of the controller.
- B (blue light): connected to the PWM output pin of the controller.
## 安装与操作
1、Connect the HuskyLens to the Raspberry Pi via the I2C interface.  
2、Follow the wiring diagram to connect the RGB LEDs to the PWM pins of the controller.  
3、Open HuskyLens, set the function to “Color Recognition” and select “Learn Multiple” mode.  
4、To learn a target color in HuskyLens, frame the color with the + character mark and press the Learn button.  
5、Use the following Python code to control the color of the RGB LEDs:  
```
import RPi.GPIO as GPIO
import serial

GPIO.setmode(GPIO.BCM)
LedPinR = 17
LedPinG = 27
LedPinB = 22

GPIO.setup(LedPinR, GPIO.OUT)
GPIO.setup(LedPinG, GPIO.OUT)
GPIO.setup(LedPinB, GPIO.OUT)

R = GPIO.PWM(LedPinR, 2000)
G = GPIO.PWM(LedPinG, 1999)
B = GPIO.PWM(LedPinB, 5000)

R.start(0)
G.start(0)
B.start(0)

def setColor(R_val, G_val, B_val):
    R.ChangeDutyCycle(R_val)
    G.ChangeDutyCycle(G_val)
    B.ChangeDutyCycle(B_val)
# Example: Setting the LED color to red
setColor(100, 0, 0)
```
6. Upload the code and run it, HuskyLens will recognize the color and output the corresponding RGB value, the color of the LED light will change in real time.
