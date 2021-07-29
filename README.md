# HomeAutomationWithPersonalAssistant
A “Smart Home” is a part of the IoT paradigm and aims to integrate home automation. Allowing objects and devices in a home to be connected to the Internet enables users to remotely monitor and control them. These include light switches that can be turned on and off by using a smartphone or by voice command. 

A Personal Voice Assistant is a technology based on AI. The software uses a device’s microphone to receive voice requests while the voice output takes place at the speaker. But the most exciting thing happens between these two actions. 

A Home Automation is the ability to do tasks automatically and monitor remotely technology based on IoT. Common tasks include turning on/off lights via Smartphone or Voice over. It is a combination of several different technologies: voice recognition, voice analysis and language processing. It is completely developed in Raspberry Pi using one of the most powerful language python-3. 

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
In LED 1: 
  * Assign to Bathroom Light
In LED 2: 
  * Assign to Bedroom Light
In LED 3: 
  * Assign to Hall Light

### Run: 
 >python3 speak_gTTS.py
