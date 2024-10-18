  __Hello__ 👋,Welcome to this tutorial on HuskyLens color recognition! In this project, you will learn how to recognize and track multiple colors using HuskyLens and output the corresponding RGB values. In the following steps 📜, you'll explore step-by-step instructions on how to set up the device, write the code, and successfully get the project up and running. Ready to begin? Let’s dive in 🚀!

- 📝 Project Description
- ✨ Functional characteristics
- 🏗  Project structure
- Required materials
- 🚀 Installation and Operation
- 🔧 Instructions for use

# Color recognition for RGB output items
## Project Description
This project implements color recognition using HuskyLens. By learning, recognizing, and tracking multiple colors, the user can obtain the RGB values of the colors in real time and automatically count the color blocks. Ambient light has a significant impact on color recognition, so it is recommended to use this feature in a well-lit environment.
- Learn and track colors: HuskyLens recognizes and tracks colors learned by the user and supports multi-color recognition.
- Automatic counting: When multiple blocks of the same color appear, they can be identified and counted at the same time.
- RGB Output: Implement the change of RGB LED light color through code to show the recognized color in real time.
## Functional characteristics
- 📏 Accurate Recognition: HuskyLens can accurately recognize and track target colors for a wide range of color scenes.
- 🎉 Highly interactive: users can adjust learning objectives in real time and get color IDs and RGB values through HuskyLens.
- 🔋 Low power consumption: low power consumption of the device, suitable for long time color recognition and tracking.
## Project structure
```
│── README.md               # Project description document
│── HuskyLens_RGB.py        # source code folder
```
## Required materials
1、HuskyLens Color Recognition Sensor  
2、Raspberry Pi (for control)  
3、RGB LED Lights  
4、DuPont wire  
5、Breadboard  
## Wiring Diagram and Pinout
### HuskyLens pinout
- Vcc (Power Positive): connected to the 5V pin of the controller.
- GND (Ground): connected to the GND pin of the controller.  
- SDA/SCL (I2C communication): connected to the I2C pins of the controller.  
### RGB LED Pinout
- R (Red): connected to the PWM output pin of the controller.  
- G (green): connected to the PWM output pin of the controller.
- B (blue light): connected to the PWM output pin of the controller.
## Step by Step - Learning Multiple Colors
1、Enter the color recognition mode: Toggle the “function button” to the left or right until “color recognition” is displayed at the top of the screen.  
2、Enter the parameter setting: Long press the “function button” to enter the second level menu of the color recognition function.  
3、Select to learn more than one color: Toggle the “Function button” to the left or right, select “Learn more than one”, and then press the “Function button” briefly.  
- Toggle the “Function Button” to the right to open the “Learn Multiple” option, at this time, the color of the progress bar changes to blue, and the square on the progress bar moves to the right side.
- Confirmation of parameters: Press the “Function button” again to confirm the setting.
![image](https://github.com/user-attachments/assets/62ecb00b-9e4a-4710-849b-bdfba5a938bb)

4、Save & Return: Toggle the “Function button” to the left, select “Save & Return” and press the “Function button” briefly.  
- The screen will prompt “Do you want to save the parameter?”. The screen will prompt “Do you want to save the parameter?”, the default choice is “Confirm”, press the “Function button” briefly to save the parameter and return to the color recognition mode automatically.
## Detecting and learning colors
1、Color Detection: Aim the “+” in the center of the HuskyLens screen at the target color block and a white box will appear on the screen to automatically frame the target color block. Adjust the angle and distance between HuskyLens and the color block so that the white box frames the entire target color block as much as possible.  
2、Learning color: After detecting the color, press the “learning button” to learn the first color, and then release the “learning button” to end the learning, the screen will display a message prompt: “Press again to continue, press other buttons to end! “Press the other keys to finish. If you need to continue to learn the next color, you can press the “Learn button” before the end of the countdown to continue learning.The color IDs displayed by HuskyLens will be sequentially labeled as “ID1”, “ID2”, “ID3”, “ID4”, “ID5”, “ID6”, “ID7”, “ID8” and “ID9”. ID1”, ‘ID2’, ‘ID3’, different colors correspond to different box colors.  
3、Identify Color: When HuskyLens encounters the same or similar color, a colored border will be displayed on the screen to frame out the color block and show the ID of that color, the size of the border will change according to the area of the color block and automatically track the color block. Multiple colors can be recognized and tracked at the same time, with different colors corresponding to different color borders.  
![image](https://github.com/user-attachments/assets/dce5d725-7389-4771-b5f9-965954caa0e8)

4、Firmware version differences: In firmware versions below V0.5.1, when multiple blocks of the same color appear, HuskyLens is unable to recognize the separated blocks at the same time, and can only recognize one block at a time.  
5、Version V0.5.1 and above: In firmware version V0.5.1 and above, HuskyLens optimizes this feature to recognize multiple blocks of the same color at the same time and can be used for the color block counting function.  
## Installation and Operation
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
