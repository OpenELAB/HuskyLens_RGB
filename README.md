# 概述
HC-04超声波测距，距离过近启动蜂鸣器
![image](https://github.com/user-attachments/assets/0428a8c5-b2ea-4c34-a014-704c58241ee2)  
# 故事（原理）
超声波模块HC-SR04（有时也被称为HC-04）是一种非接触式的距离传感器，它通过发送和接收超声波信号来测量与目标物体之间的距离。这种模块在机器人技术、自动化、物体定位和避障等多个领域都有广泛应用。
- 非接触测量：无需与目标物体直接接触，即可测量距离。
- 测量准确：在一定的测量范围内，能够提供相对准确的距离数据。
- 易于集成：模块化的设计使得它很容易集成到各种电子项目中。
- 低成本：与其他类型的传感器相比，HC-SR04通常价格较为亲民  

根据时序图编写代码就能正确的接受到距离数据了
# 时序图
![image](https://github.com/user-attachments/assets/31f4b7da-3122-44a5-9d48-86e2d1de288f)

## 我们制作这个项目所需的材料
1. Arduino UNO
2. HC-04超声波模块
3. 串口线
4. 公对公杜邦线4根
5. 面包板一个
6. 蜂鸣器一个
## 引脚介绍以及接线
### Vcc（正极电源）
- 功能：为模块提供电源。
- 连接：通常连接到开发板或控制器的5V电源输出。
### GND（负极电源/地线）
- 功能：作为模块的公共地线。
- 连接：连接到开发板或控制器的地线（GND）引脚。
### Trig（触发信号输入）
- 功能：用于触发超声波的发送。
- 操作：向此引脚发送一个至少10us的高电平信号，模块就会发送超声波并等待回声。
- 连接：连接到开发板或控制器的数字输出引脚。
### Echo（回声信号输出）
- 功能：当超声波遇到障碍物并返回时，此引脚会输出一个高电平信号，其持续时间与超声波往返时间成正比。
- 测量：通过测量Echo引脚高电平持续的时间（单位通常为微秒），并结合超声波在空气中的传播速度（约340m/s），可以计算出超声波与目标物体之间的距离。
- 连接：连接到开发板或控制器的数字输入引脚，同时可能需要连接到一个外部中断引脚以便更精确地测量时间。
## 具体步骤
1. 使用串口线连接Arduino UNO。
![image](https://github.com/user-attachments/assets/5a99677b-0d9c-4fd6-a7a5-13b5a9502013)

2. 按照接线图连接Arduino和HC-04，再将串口连接至电脑USB口。
3. 选择想要实现的效果的相应文件，实现正数计时。在Arduino IDE中写入代码
``` 
int trigPin = 11;    //Trig
int echoPin = 12;    //Echo
long duration, cm, inches;
 
void setup() {
  //Serial Port begin
  Serial.begin (9600);
  //Define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
 
void loop()
{
  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  duration = pulseIn(echoPin, HIGH);
 
  // convert the time into a distance
  cm = (duration/2) / 29.1;
  inches = (duration/2) / 74; 
  
  Serial.print(inches);
  Serial.print("in, ");
  Serial.print(cm);
  Serial.print("cm");
  Serial.println();
  
  delay(1000);
}
```
4.  连接好Arduino和模块的线后，点击编译以及上传
  ![image](https://github.com/user-attachments/assets/048771d6-e1d4-47a1-b90c-5c3ed1168573)
5. 打开串口查看当前距离数值
实验现象

当HC-04超声波模块检测到，距离小于25CM时将会开启蜂鸣器
暂时无法在飞书文档外展示此内容

