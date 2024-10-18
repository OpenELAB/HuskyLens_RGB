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
## 操作步骤 - 学习多个颜色
1、进入颜色识别模式：向左或向右拨动“功能按键”，直到屏幕顶部显示“颜色识别”。  
2、进入参数设置：长按“功能按键”进入颜色识别功能的二级菜单。  
3、选择学习多个颜色：向左或向右拨动“功能按键”，选中“学习多个”，然后短按“功能按键”。    
- 向右拨动“功能按键”开启“学习多个”选项，此时进度条颜色变为蓝色，并且进度条上的方块移动到右侧。
- 确认参数：再短按“功能按键”确认设置。

4、保存并返回：向左拨动“功能按键”，选中“保存并返回”，短按“功能按键”。  
- 屏幕会提示“是否保存参数？”，默认选择“确认”，短按“功能按键”保存参数并自动返回颜色识别模式。
## 侦测与学习颜色
1、侦测颜色：将HuskyLens屏幕中央的“+”字对准目标颜色块，屏幕上会出现一个白色方框，自动框选目标颜色块。调整HuskyLens与颜色块的角度和距离，使白色方框尽量框住整个目标色块。  
2、学习颜色：侦测到颜色后，按下“学习按键”学习第一种颜色，然后松开“学习按键”结束学习，屏幕上会显示消息提示：“再按一次继续，按其他按键结束”。如果需要继续学习下一个颜色，可以在倒计时结束前按下“学习按键”，继续学习。HuskyLens显示的颜色ID会按顺序依次标注为“ID1”、“ID2”、“ID3”，不同颜色对应不同的方框颜色。  
3、识别颜色：当HuskyLens遇到相同或相近的颜色时，屏幕上会显示彩色边框框选出色块，并显示该颜色的ID，边框大小会随色块的面积变化，并自动跟踪色块。多种颜色可以同时被识别和追踪，不同颜色对应不同颜色的边框。  
4、固件版本差异：在V0.5.1版本以下的固件中，当多个相同颜色的色块出现时，HuskyLens无法同时识别相隔的色块，一次只能识别一个色块。  
5、V0.5.1版本及以上：在V0.5.1及以上版本的固件中，HuskyLens优化了该功能，可以同时识别多个相同颜色的色块，并可用于色块计数功能。
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
