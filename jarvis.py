from datetime import datetime  
import excel     
import instadownloader
import smtplib
import PyPDF2
from time import sleep,time
import time
import webbrowser
import pip._vendor.requests 
import cv2
import pyttsx3
import os
import requests
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit as pwk
import smtplib
import sys
import pyautogui
import pyjokes
from PyQt5 import QtWidgets,QtCore,QtGui
from jarvisUi import Ui_jarvisUi

from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi


engine  = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



def wish(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning ")
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I am Assis sir, How can I help you')

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('aakashgupta_ce_2020@ltce.in','11k1shgupta')
    server.sendmail('aakashgupta_ce_2020@ltce.in', to,content)
    server.close()

def news():
    url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'
    print(url)
    page = requests.get(url).json()
    articles = page['articles']
    head=[]
    day =["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"{day[i]} news is:  {head[i]}" ) 

def pdf_reader():
    book = open('CN-Experiment1.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Sir total pages in this book are {pages}")
    speak("sir enter the page number I have to read")
    pg = int(input("Enter the page numebr: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text) 


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takeCommand(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold =1
            audio = r.listen(source,timeout=10,phrase_time_limit=5)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio,language='en-in')
            print(f"user said: {self.query}")

        except Exception as e:
            speak('Phir se boliye sir')
            return 'none'
        return self.query

    
    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takeCommand().lower()

            # Logic for Tasks

            if 'open notepad' in self.query:
                path = 'C:\\Windows\\System32\\notepad.exe'
                os.startfile(path)

            elif 'open command prompt' in self.query:
                os.system('start cmd')

            elif 'open vs code' in self.query:
                path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)

            elif 'open camera' in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                    cap.release()
                    cv2.destroyAllWindows()

            elif 'play song' in self.query:
                music_dir = 'C:\\Users\\Sanika'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))

            elif 'ip address' in self.query:
                ip = pip._vendor.requests.get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")

            elif 'wikipedia' in self.query:
                speak('Searching Wikipedia')
                self.query = self.query.replace('wikipedia',"")
                results = wikipedia.summary(self.query,sentences=2)
                speak(results)

    # youtube 
            elif 'open youtube' in self.query:
                speak("Sir, what should I search")
                cm = self.takeCommand().lower()
                pwk.playonyt(cm)

            elif 'play next song on youtube' in self.query:
                pyautogui.keyDown("shift")
                pyautogui.press("N")
                time,sleep(1)
                pyautogui.keyUp("shift")

            elif 'play before song on youtube' in self.query:
                pyautogui.keyDown("shift")
                pyautogui.press("p")
                time,sleep(1)
                pyautogui.keyUp("shift")

            elif 'pause video' in self.query:
                pyautogui.press("K")

            elif 'play video' in self.query:
                pyautogui.press("K")

            elif 'rewind video' in self.query:
                pyautogui.press("j")

            elif 'forward video' in self.query:
                pyautogui.press("l")
            
            elif 'full screen' in self.query:
                pyautogui.press("f")

            elif 'mini player' in self.query:
                pyautogui.press("i")

            elif 'mute the video' in self.query:
                pyautogui.press("m")

            elif 'unmute the video' in self.query:
                pyautogui.press("m")
    # youtube

    #Chrome
            elif 'open google' in self.query:
                speak('sir,whta should i search')
                cm = self.takeCommand().lower()
                webbrowser.open(f"{cm}")

            elif 'open new tab' in self.query:
                pyautogui.keyDown('ctrl')
                pyautogui.press('n')
                pyautogui.keyUp('ctrl')
                speak('sir,whta should i search')
                cm = self.takeCommand().lower()
                pyautogui.keyDown('ctrl')
                pyautogui.press('l')
                pyautogui.keyUp('ctrl')
                pwk.search(cm)


            

    # social media 
            elif 'facebook' in self.query:
                webbrowser.open('www.facebook.com')

            elif 'open instagram' in self.query:
                webbrowser.open('www.instagram.com')

            elif 'instagram profile' in self.query:
                speak("Sir Please enter the user name correctly")
                name = input("Enter Username here: ")
                # webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profileof the user {name}")
                # time.sleep(5)
                speak("Sir would you like to download the profile pic")
                cond= 'yes'
                if 'yes' in cond:
                    mod = instadownloader.instaloader()
                    mod.download_profile(name,profile_pic_only = True)
                    speak("Profile pic is saved in our main folder sir")
                else:
                    pass



            elif 'send message' in self.query:
                pwk.sendwhatmsg("+918291588459","padhai karo",16,36)
                
            elif 'send email' in self.query:
                try:
                    speak("What should i send")
                    content = 'jdkncknnck nink nk n'
                    to = 'gujarsanika3008@gmail.com'
                    sendEmail(to,content)
                    speak("Email has been send")
                except Exception as e:
                    print(e)
                    speak("Sorry sir, email send nhi hua!")
    # social media 

    # excel 

            elif 'open excel sheet' in self.query:
                speak("Sir Please enter the name of the file")
                cmd = input()
                cmd = cmd +'.xlsx'
                speak("Sir in which root directory should I search")
                sec_cmd = input()
                sec_cmd = sec_cmd+':'
                def find_files(filename, search_path):
                    result = []
                    for root, dir, files in os.walk(search_path):
                        if filename in files:
                            result.append(os.path.join(root, filename))
                    return result

                try:
                    if find_files(cmd,sec_cmd):
                        wb = excel.load_workbook()
                        ws = wb.active
                        speak('Sheet is open sir')
                    else:
                        speak('Sir file not exist')
                except Exception as e:
                    print(e)
                    speak('Sorry sir , there is an error for opening of file')
            elif 'search name' in self.query:
                try:
                    # speak('Sir which name i have to search')
                    name = self.takeCommand()
                    s = excel.excel()
                    
                    s.title()
                    print(s.get_name_and_row_num(name))

                except:
                    speak("there is some problem sir")

            elif 'show row values' in self.query:
                s.show_columns_with_values()

            elif 'save sheet' in self.query:
                speak('which sheet should i close')
                sheet = input()
                sheet  = sheet + '.xlsx'
                wb.save(sheet)
                speak("sir sheet is saved")
            
            # search files 
            elif 'search file' in self.query:
                speak("sir which file should i search")
                filename  = input()
                seconds = int(time.time())
                last_timer = seconds +20
                def find_files(filename, search_path):
                    result = []
                    for root, dir, files in os.walk(search_path):
                        if int(time.time()) == last_timer:
                            break
                        else:
                            if filename in files:
                                result.append(os.path.join(root, filename))
                    return result

                switcher  = {
                    1:print("In C Drive ",find_files(filename,'C:')),
                    2:print("In D Drive ",find_files(filename,'D:')),
                    3:print("In E Drive ",find_files(filename,'E:'))
                }

                

            elif 'close notepad' in self.query:
                speak("okay sir , Closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif 'screenshot' in self.query:
                speak("Sir what sholud be the name of the file")
                name = self.takeCommand().lower()
                speak("sir wait for few seconds")
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("SS is taken sir")
                
            elif 'read pdf' in self.query:
                pdf_reader()

            elif 'set alarm' in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==22:
                    music_dir = ''
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir,songs[0]))

            elif 'tell me a joke' in self.query:
                joke = pyjokes.get_joke()
                speak(joke)


            elif 'change tab' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif 'tell me news' in self.query:
                speak('Please wait sir , fetching the latest news')
                news() 

            elif 'where i am' in self.query:
                speak("Getting loaction")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    url = f'https://get.geojs.io/v1/ip/geo/{ipAdd}.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"Sir we are in {city} city of {country} country")
                except Exception as e:
                    print("husdjjsdnx",e)
                    speak("sorry sir , Due to some issue I am not able to find the location.")    

            elif 'shutdown the system' in self.query:
                os.system('shutdown /s /t 5')

            elif 'restart the system' in self.query:
                os.system('shutdown /r /t 5')

            elif 'no thanks' in self.query:
                speak('ok sir')
                sys.exit()
            speak("next job")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:\pythoncollege\iron man.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:\pythoncollege\Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()    
    def showTime(self):
        currentTime = QTime.currentTime()
        date = QDate.currentDate()
        label_time = currentTime.toString('hh:mm:ss')
        label_date = date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
