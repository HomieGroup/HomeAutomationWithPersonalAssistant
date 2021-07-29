# HomeAutomationWithPersonalAssistant:
A **“Smart Home”** is a part of the IoT paradigm and aims to integrate home automation. Allowing objects and devices in a home to be connected to the Internet enables users to remotely monitor and control them. These include light switches that can be turned on and off by using a smartphone or by voice command. 

A **Personal Voice Assistant** is a technology based on AI. The software uses a device’s microphone to receive voice requests while the voice output takes place at the speaker. But the most exciting thing happens between these two actions. 

A **Home Automation** is the ability to do tasks automatically and monitor remotely technology based on **IoT**. Common tasks include turning on/off lights via Smartphone or Voice over. It is a combination of several different technologies: voice recognition, voice analysis and language processing. It is completely developed in **Raspberry Pi** using one of the most powerful language **python-3.** 

# Software requirements:
  1. Raspbian OS lite
  2. Python 3
# Hardware requirements:
  1. Raspberry Pi with Wi-Fi Module
  2. Microphone (I used USB Audio card instead of Seperated USB microphones)
  3. Speaker
  4. Raspberry Power Supply
# Other requirements:
  1. Wi-Fi Network
  2. Relay Switch
  3. Jumper Wires

### Python Library:
  1. SpeechRecognition
  2. Youtube-dl
  3. gTTS
  4. RPi.GPIO
  5. datetime
  6. Wikipedia
  7. Threading
  8. Flask
  9. Time
### Linux Library:
  1. python-pyaudio
  2. python3-pyaudio 
  3. Flac
  4. mgp321
  5. python3-gst-1.0
  6. libgstreamer1.0-dev
  7. gstreamer-tools
### Git Repositories:
  1. git clone https://github.com/uditkarode/youtube-cli  (Thank You @Uditkarode)
### Connections: 
![image](https://user-images.githubusercontent.com/88142443/127484274-388d37be-d027-42bc-9d2b-a7921e698c72.png)
> * In LED 1: 
  >  Assign to Bathroom Light
> * In LED 2: 
  >  Assign to Bedroom Light
> * In LED 3: 
  >  Assign to Hall Light

### Run: 
 >python3 speak_gTTS.py

### Use case diagrams:
![adfafd](https://user-images.githubusercontent.com/88142443/127485239-42f6b7a6-5d1c-4673-83e9-4c63bb5387cd.JPG)

### Implementation:
  1. The U.S. English language model provides context to distinguish the work.
  2. All the performance and speed of response are depends on Raspberry Hardware Configuration as well as Internet Speed.
  3. Use Good Quality of Microphones.
  4. All the appliances should be connected in same network.
  5. Call “hey Buddy”, "hello buddy" or "hi buddy" to Wake up and Response, every time after Completing previous work.
  6. If there is no response means that wrong input and give command again from starting.
  7. If we want to search any thing in Wikipedia, Say the any sentences which include Wikipedia, after get response from raspberry, give the command to search it. After the retrieving Information, It Will response and giving information about 2 lines.
  8. To operate devices:
      1. Using Voice Over Command to Turning ON/OFF of Bathroom, Bedroom or Hall Light respectively, Say “ Bathroom Light On” vice-versa.
      2. Using Webpage to Turning ON/OFF of Bathroom, Bedroom or Hall Light, Go to Browser and search “localhost:5010” / “(Assign IP of Raspberry Pi):5010”. Ex. “192.168.43.167:5010”.
  9. Raspberry Pi GP I/O pin assign as
      1. GPIO 17: Bathroom Light
      2. GPIO 27: Bedroom Light
      3. GPIO 22: Hall Light

