import speech_recognition as sr
from gtts import gTTS
import RPi.GPIO as GPIO      
import os
import datetime
import wikipedia
import threading
from time import sleep
from flask import Flask
from flask import Flask, render_template
import time

app = Flask(__name__)
r= sr.Recognizer()
led1 = 17
led2 = 27
led3 = 22
num = 1
text = {}
text1 = {}
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.output(led1, 1)
GPIO.output(led2, 1)
GPIO.output(led3, 1)
print("Done")

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/A')
def led1on():
    GPIO.output(led1, 0)
    return render_template('index.html')

@app.route('/a')
def led1off():
    data1="a"
    GPIO.output(led1, 1)
    return render_template('index.html')
                
@app.route('/B')
def led2on():
    data1="B"
    GPIO.output(led2, 0)
    return render_template('index.html')

@app.route('/b')
def led2off():
    data1="b"
    GPIO.output(led2, 1)
    return render_template('index.html')

@app.route('/C')
def led3on():
    data1="C"
    GPIO.output(led3, 0)
    return render_template('index.html')

@app.route('/c')
def led3off():
    data1="c"
    GPIO.output(led3, 1)
    return render_template('index.html')


def assistant_speaks(output):
    global num
    num += 1
    toSpeak = gTTS(text = output, lang ='en-in', slow= False)
    file = "tempOutputAudio/"+str(num)+".mp3"
    toSpeak.save(file)
    os.system("mpv " +file)
    #playsound.playsound(file, True) 
    os.remove(file)
def listen1():
    with sr.Microphone(device_index = 1) as source:
         r.adjust_for_ambient_noise(source)
         print("Say Something");
         r.pause_threshold= 0.5
         audio = r.listen(source)
         print("got it");

    try: 
         text1 = r.recognize_google(audio).lower()
         print ("you said: " + text1);
         return text1; 
    except sr.UnknownValueError: 
         #call(["espeak", "-s140  -ven+18 -z" , "Google Speech Recognition could not understand"])
         #assistant_speaks("Speak Again")
         print("Speak Again")
         text1={} 
         return text1;
def listen():
    with sr.Microphone(device_index = 1) as source:
         r.adjust_for_ambient_noise(source)
         print("Say Something");
         r.pause_threshold= 0.5
         audio = r.listen(source)
         print("got it");

    try: 
         text1 = r.recognize_google(audio).lower()
         print ("you said: " + text1);
         return text1; 
    except sr.UnknownValueError: 
         #call(["espeak", "-s140  -ven+18 -z" , "Google Speech Recognition could not understand"])
         #assistant_speaks("Speak Again")
         print("Speak Again")
         text1={} 
         return text1;

def main(text):
       text = listen()
       if 'bedroom light on' in text:
          GPIO.output(led1 , 0)
          assistant_speaks("okay  Sir, Switching ON the Lights")
          #call(["espeak", "-ven-us+f2","-s200", "okay  Sir, Switching ON the Lights"])
          print ("Bedroom Lights on")
       elif 'bathroom light on' in text:
          GPIO.output(led2 , 0)
          assistant_speaks("okay  Sir, Switching ON the Lights")
          #call(["espeak", "-ven-us+f2","-s200", "okay  Sir, Switching ON the Lights"])
          print ("Lights on");
       elif 'bedroom light off' in text:
          GPIO.output(led1 , 1)
          assistant_speaks("okay  Sir, Switching off the Lights")
          #call(["espeak", "-ven-us+f2","-s200", "okay  Sir, Switching off the Lights"])
          print ("Lights Off");
       elif 'bathroom light off' in text:
          GPIO.output(led2 , 1)
          assistant_speaks("okay  Sir, Switching off the Lights")
          #call(["espeak", "-ven-us+f2","-s200", "okay  Sir, Switching off the Lights"])
          print ("Lights Off");
       elif 'hall light on' in text:
          GPIO.output(led2 , 0)
          assistant_speaks("okay  Sir, Switching ON the Lights")
          #call(["espeak", "-ven-us+f2","-s200", "okay  Sir, Switching ON the Lights"])
          print ("Lights on");
       elif 'hall light off' in text:
          GPIO.output(led1 , 1)
          assistant_speaks("okay  Sir, Switching off the Lights")
          #call(["espeak", "-ven-us+f2","-s200", "okay  Sir, Switching off the Lights"])
          print ("Lights Off");
       elif text == 'thank you' or text == 'thanks':
          assistant_speaks("Its My pleasure")
          #call(["espeak", "-ven-us+f2","-s180"," Its My pleasure"])
       elif 'date' in text:
          xd = datetime.datetime.now()
          yd=xd.strftime("%d/%B/%Y")
          print(yd)
          assistant_speaks(yd)
          #os.system("date +%I:%M%p | espeak -ven-us+f2 -s200")
       elif 'time' in text:
          xt = datetime.datetime.now()
          yt=xt.strftime("%I:%M %p")
          print(yt)
          assistant_speaks(yt)
          #os.system("date +%d%B%Y | espeak -ven-us+f2 -s200")
       elif 'play' in text:
          class playYT:
            def __init__(self):
                self.pid=3
            def YT(self):
                #assistant_speaks("Heres some result from youtube")
                self.pid = os.getpid()
                print(self.pid)
                os.system("ytm -p "+text)
            def back(self):
                while (1):
                    YT={}
                    YT=listen1()
                    #sleep(30)
                    print(self.pid)
                    if 'exit' in YT or 'thank you' in YT:
                        os.system("killall mpv")
                        break
            def run(self):
                t1 = threading.Thread(target=self.YT)
                t2 = threading.Thread(target=self.back)
                t1.start()
                t2.start()
                t1.join()
                t2.join()
                print(self.pid)
          d=playYT()
          d.run()
       elif 'wikipedia' in text:
          assistant_speaks("what do you want to search in wikipedia")
          textwiki= listen()
          xwiki=wikipedia.summary(textwiki, sentences=2)
          assistant_speaks(xwiki)
          
       text = {}
if __name__ == '__main__':
    class mainRoute:
        def __init__(self):
            self.pid=0
        def Route(self):
            app.run(host='192.168.43.167',port=5010)
        def speaker(self):
            while(1):
                text1 = listen1()
                if 'hey' in text1: 
                    text = {}
                    assistant_speaks("yes sir")
                    main(text)
                    text1 = {}
        def run(self):
            t1 = threading.Thread(target=self.Route)
            t2 = threading.Thread(target=self.speaker)
            t1.start()
            t2.start()
            t1.join()
            t2.join()
            print(self.pid)
    d=mainRoute()
    d.run()