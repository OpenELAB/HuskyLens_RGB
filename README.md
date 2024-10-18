  __Hello__ 👋，欢迎来到这个基于HuskyLens二哈识图的颜色识别执行动作的教程！在这个项目中，你将学习如何使用HuskyLens识别和追踪多种颜色，并输出相应的RGB值。在接下来的步骤 📜，你将逐步探索如何设置设备、编写代码，并将项目成功运行起来。准备好了吗？让我们开始吧 🚀！

- 📝 项目描述
- ✨ 功能特性
- 🏗 项目结构
- 🚀 安装与操作
- 🔧 使用说明

# 颜色识别进行RGB输出项目
## 项目描述
本项目基于HuskyLens实现颜色识别，通过学习、识别并追踪多种颜色，用户可以实时获取颜色的RGB值，并对颜色块进行自动计数。环境光线对颜色识别有很大影响，建议在光线适中的环境中使用该功能。
- 学习并追踪颜色：HuskyLens可以识别并追踪用户学习的颜色，支持多颜色的识别。
- 自动计数：当出现多个相同颜色的色块时，可以同时识别并计数。
- RGB输出：通过代码实现RGB LED灯颜色的改变，实时展示识别出的颜色。
## 功能特性
- 📏 精确识别：HuskyLens可以精确地识别并追踪目标颜色，适用于多种颜色场景。
- 🎉 高互动性：用户可以实时调整学习目标，并通过HuskyLens获取颜色ID和RGB值。
- 🔋 低功耗：设备功耗低，适合长时间的颜色识别与追踪。
## 项目结构
```
│── README.md               # 项目说明文件
│── ColorRecognition        # 源代码文件夹
  │── main.py               # 主代码文件
  │── RGBControl.py         # RGB控制代码
  │── HuskyLens.py          # HuskyLens接口代码
```
## 所需材料
1、HuskyLens 颜色识别传感器  
2、Arduino或树莓派（用于控制）  
3、RGB LED灯  
4、杜邦线  
5、面包板  
## 接线图与引脚介绍
### HuskyLens 引脚
- Vcc（电源正极）：连接到控制器的5V引脚。
- GND（地线）：连接到控制器的GND引脚。
- SDA/SCL（I2C通信）：连接到控制器的I2C引脚。
### RGB LED 引脚
- R（红灯）：连接到控制器的PWM输出引脚。
- G（绿灯）：连接到控制器的PWM输出引脚。
- B（蓝灯）：连接到控制器的PWM输出引脚。
## 安装与操作
1、通过I2C接口将HuskyLens连接到树莓派。  
2、按照接线图将RGB LED灯连接到控制器的PWM引脚。  
3、打开HuskyLens，将功能设置为“颜色识别”，并选择“学习多个”模式。  
4、在HuskyLens中学习目标颜色，通过+字标记框住颜色并按下学习按键。  
5、使用以下Python代码控制RGB LED灯的颜色：  
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
# 示例：设定LED颜色为红色
setColor(100, 0, 0)
```
6、上传代码并运行，HuskyLens将识别颜色并输出相应的RGB值，LED灯的颜色将实时变化。  
