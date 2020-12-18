import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import subprocess
import cv2
import time
import pyjokes
import face_recognition
import cv2
import numpy as np
import pyautogui
from requests import get
import pywhatkit as kit
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi


engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('VSD547-VGHE57128')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)
engine.setProperty('rate',180)


def speak(audio):
    print('JARVIS: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def wish():
    currentH = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if currentH >= 0 and currentH < 12:
        speak(f'Good Morning Sir, its {tt}')

    elif currentH >= 12 and currentH < 18:
        speak(f'Good Afternoon Sir, its {tt}')

    else:
        speak(f'Good Evening Sir, its {tt}')
        speak('Hello Sir, I am  JARVIS!')
        speak('What can I do for you?')
        

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()

    def run(self):
        self.TaskExecution()

    def takecommand(self):
            r = sr.Recognizer()                                                                                   
            with sr.Microphone() as source:                                                                       
                print("Listening...")
                r.pause_threshold =  1
                audio = r.listen(source)
            try:
                print('Recognize...')
                self.query = r.recognize_google(audio, language='en-in')
                print(f'SIR: {self.query}')
                
            except Exception as e:
                return 'none'
            self.query = self.query.lower()
            return self.query






    def TaskExecution(self):
        wish()
        while True:        
            self.query = self.takecommand()
        
            
            if 'open youtube' in self.query:
                speak('okay Sir')
                webbrowser.open('www.youtube.com')

            elif 'open notepad' in self.query:
                speak('okay sir, opening notepad')
                npath = (r'C:\\Windows\\system32\\notepad.exe')
                os.startfile(npath)

            elif 'open google' in self.query:
                speak('okay Sir,opening Google')
                webbrowser.open('www.google.com')

            elif 'send message' in self.query:
                kit.sendwhatmsg('+916200770706', 'hi this is jarvis',2,25)    

            elif 'take screenshot' in self.query:
                speak('sir, please tell me the name for this screenshot file')
                name = self.takecommand()
                speak('okay sir, please wait i am taking the screenshot')
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak('i am done sir, the screenshot is saved in our main folder')     

            elif 'open my github id' in self.query:
                speak('okay Sir, opening your GITHUB id')
                webbrowser.open('https://github.com/LinearProgramming/Hello-World')

            elif 'open gmail' in self.query:
                speak('okay Sir, opening gmail')
                webbrowser.open('www.gmail.com')
           
            elif 'open powerpoint' in self.query:
                speak('okay boss, opening powerpoint')
                subprocess.call(r'C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.EXE')    

            elif 'open winword' in self.query:
                speak('okay Sir, opening winword')
                subprocess.call(r'C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE')

            elif 'open excel' in self.query:
                speak('okay Sir, opening excel')
                subprocess.call(r'C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.EXE')    

            elif 'open obs studio' in self.query:
                speak('okay Sir, opening obs studio')
                subprocess.call(r'E:\\screen recorder\\obs-studio\\bin\\64bit\\obs64.exe')

            elif 'open iron man' in self.query:
                speak('okay Sir, opening iron man')
                subprocess.call(r'E:\\Iron Man 2008 PC Game\\GameLauncher.exe')

            elif 'reminder' in self.query :
                speak("What is the reminder?")
                data = self.takecommand()
                speak("reminder set")
                reminder_file = open("data.txt", 'a')
                reminder_file.write('\n')
                reminder_file.write(data)
                reminder_file.close()

    #reading reminder list

            elif 'remember' in self.query:
                reminder_file = open("data.txt", 'r')
                speak("You said me to remember that: " + reminder_file.read())  
                

            elif 'switch window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif 'detect face' in self.query:
                speak('okay Sir! runing face detection mode')
                #for getting a reference from webcam
                video_capture = cv2.VideoCapture(0)


                #load some images you want to recognise

                Aakanksha_image = face_recognition.load_image_file("Aakanksha.jpg")
                Aakanksha_face_encoding = face_recognition.face_encodings(Aakanksha_image)[0]

                Aditi_image = face_recognition.load_image_file("Aditi.jpg")
                Aditi_face_encoding = face_recognition.face_encodings(Aditi_image)[0]

                Aditya_image = face_recognition.load_image_file("Aditya.jpg")
                Aditya_face_encoding = face_recognition.face_encodings(Aditya_image)[0]

                Priya_image = face_recognition.load_image_file("Priya.jpg")
                Priya_face_encoding = face_recognition.face_encodings(Priya_image)[0]

                Reena_image = face_recognition.load_image_file("Reena.jpg")
                Reena_face_encoding = face_recognition.face_encodings(Reena_image)[0]

                Sanjay_image = face_recognition.load_image_file("Sanjay.jpg")
                Sanjay_face_encoding = face_recognition.face_encodings(Sanjay_image)[0]

                Vikas_image = face_recognition.load_image_file("Vikas.jpg")
                Vikas_face_encoding = face_recognition.face_encodings(Vikas_image)[0]

                Vaibhav_image = face_recognition.load_image_file("Vaibhav.jpg")
                Vaibhav_face_encoding = face_recognition.face_encodings(Vaibhav_image)[0]

                Vivek_image = face_recognition.load_image_file("Vivek.jpg")
                Vivek_face_encoding = face_recognition.face_encodings(Vivek_image)[0]

                Ansh_image = face_recognition.load_image_file("Ansh.jpg")
                Ansh_face_encoding = face_recognition.face_encodings(Ansh_image)[0]

                Anchala_image = face_recognition.load_image_file("Anchala.jpg")
                Anchala_face_encoding = face_recognition.face_encodings(Anchala_image)[0]

                Alok_image = face_recognition.load_image_file("Alok.jpg")
                Alok_face_encoding = face_recognition.face_encodings(Alok_image)[0]

                Manoj_image = face_recognition.load_image_file("Manoj.jpg")
                Manoj_face_encoding = face_recognition.face_encodings(Manoj_image)[0]

                Abhimanyu_image = face_recognition.load_image_file("Abhimanyu.jpg")
                Abhimanyu_face_encoding = face_recognition.face_encodings(Abhimanyu_image)[0]

                Abhinav_image = face_recognition.load_image_file("Abhinav.jpg")
                Abhinav_face_encoding = face_recognition.face_encodings(Abhinav_image)[0]

                #create arrays of known_face_encodings & names
                known_face_encodings = [
                    Aakanksha_face_encoding,
                    Aditi_face_encoding,
                    Aditya_face_encoding,
                    Priya_face_encoding,
                    Reena_face_encoding,
                    Sanjay_face_encoding,
                    Vikas_face_encoding,
                    Vaibhav_face_encoding,
                    Vivek_face_encoding,
                    Ansh_face_encoding,
                    Anchala_face_encoding,
                    Alok_face_encoding,
                    Manoj_face_encoding,
                    Abhimanyu_face_encoding,
                    Abhinav_face_encoding
                ]

                known_face_names = [
                    "Aakanksha",
                    "Aditi",
                    "Aditya",
                    "Priya",
                    "Reena",
                    "Sanjay",
                    "Vikas",
                    "Vaibhav",
                    "Vivek",
                    "Ansh",
                    "Anchala",
                    "Alok",
                    "Manoj",
                    "Abhimanyu",
                    "Abhinav"
                ]

                face_locations = []
                face_encodings = []
                face_names = []


                process_this_frame = True

                while True :
                    #for grab a frame
                    ret, frame = video_capture.read() 
                    #resize the frame for faster recognition
                    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
                    #convert bgr colour frame into rgb colour frame for face recognition
                    rgb_small_frame = small_frame[:,:,::-1]

                    if process_this_frame :
                        #for find the all faces and face encodings in the current frame
                        face_locations = face_recognition.face_locations(rgb_small_frame)
                        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)

                        face_names = []

                        for face_encoding in face_encodings :
                            #match the displayed faces in the frame with known faces 
                            matches = face_recognition.compare_faces(known_face_encodings,face_encoding)

                            name = 'unknown'

                            face_distances = face_recognition.face_distance(known_face_encodings,face_encoding)
                            best_match_index = np.argmin(face_distances)

                            #if the face is matched with known face append the name of the known face
                            if matches[best_match_index] :
                                name = known_face_names[best_match_index]
                            face_names.append(name)
        
                    process_this_frame = not process_this_frame

                    #display the results
                    for (top,right,bottom,left), name in zip(face_locations,face_names) :
                        top *= 4
                        right *= 4
                        bottom *= 4
                        left *= 4

                        #draw a box around the face displayed in the frame
                        cv2.rectangle(frame,(left,top),(right,bottom),(255,0,0),2)
                        #draw a label with a name below the face
                        cv2.rectangle(frame,(left,bottom-35),(right,bottom),(255,0,0),cv2.FILLED)
                        #font for the text
                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(frame,name,(left+6,bottom-6),font,1.0,(255,255,255),1)

                    #Display resulting frame 
                    cv2.imshow('Face_Detection',frame)

                    #exit key for quit a program
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                 #release handle to the webcam
                video_capture.release()
                cv2.destroyAllWindows()

            
            elif 'shutdown' in self.query:
                speak('okay Sir, work in progress')
                os.system('shutdown -s')

            elif 'play invincible music' in self.query:
                speak('okay Sir')
                webbrowser.open('https://www.youtube.com/watch?v=Sf9NSd_2avA')     

            elif 'tell me joke' in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'set alarm' in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn==22:
                    music_dir = 'E:\song\Bulleya.mp3'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            elif 'restart' in self.query:
                speak('okay Sir, work in progress')
                os.system('shutdown /r /t 5')

            elif "what\'s up" in self.query or 'how are you' in self.query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                speak(random.choice(stMsgs))

            elif 'email' in self.query:
                speak('Who is the recipient? ')
                recipient = self.takecommand()
                if 'me' in recipient:
                    try:
                        speak('What should I say? ')
                        content = self.takecommand()
            
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.ehlo()
                        server.starttls()
                        server.login("Your_Username", 'Your_Password')
                        server.sendmail('Your_Username', "Recipient_Username", content)
                        server.close()
                        speak('Email sent!')

                    except:
                        speak('Sorry Boss! I am unable to send your message at this moment!')

            elif 'nothing' in self.query or 'abort' in self.query or 'stop' in self.query:
                speak('okay Sir')
                speak('Bye Sir,have a good day.')
                sys.exit()
               
            elif 'hello' in self.query:
                speak('Hello Sir')

            elif 'are you here' in self.query:
                speak('Yes Sir, I am always here for you boss')

            elif 'bye' in self.query:
                speak('Bye Sir, have a good day.')
                sys.exit()
              
            elif 'play music' in self.query:
                music_folder = ('E:/song/')
                music = ['Dil_Mein_Mars_Hai_-_Mission_Mangal__Akshay__Vidya__Sonakshi__Taapsee__Benny_Dayal_&_Vibha_Saraf(128kbps)', 'Baaki_Baatein_Peene_Baad_-_Arjun_Kanungo_feat._Badshah___Nikke_Nikke_Shots__', 'Jab_Tak', 'Besabriyaan', 'Daru_party', 'Kaun_Tujhe', 'Main_Hoon', 'Daspacito_Justin_Bieber_Luis_Fonsi', 'Commando_2__Hare_Krishna_Hare_Ram___Vidyut_Jammwal,_Adah_Sharma,_Esha_Gupta,', 'Imran_Khan_-_Satisfya_(Official_Music_Video)(128kbps)', 'Ik_Vaari_Aa___Raabta___Sushant_Singh_Rajput___Kriti_Sanon___Pritam_Arijit_Singh_', 'Ding_Dang_-_Full_song_with_lyrics__7C_Munna_Michael_2017__7C_Tiger_Shroff__26_Nidhhi_A', 'Feel_The_Rhythm_-_Full_Audio_Song__7C_Munna_Michael__7C_Tiger_Shroff__26_Nidhhi_Agerwa', 'Moto_(Official_Video)_Ajay_Hooda__Diler_Kharkiya__Anjali_Raghav__Latest_Haryanvi_Song_2020(128kbps)']
                random_music = music_folder + random.choice(music) + '.mp3'
                os.system(random_music)
                speak('Okay Sir, here is your music! Enjoy!')
                

            else:
                self.query = self.query
                speak('Searching...')
                try:
                    try:
                        res = client.query(self.query)
                        results = next(res.results).text
                        speak('WOLFRAM-ALPHA says - ')
                        speak('Got it.')
                        speak(results)
                        
                    except:
                        results = wikipedia.summary(self.query, sentences=2)
                        speak('Got it.')
                        speak('WIKIPEDIA says - ')
                        speak(results)
            
                except:
                    webbrowser.open('www.google.com')
            
            speak('Next Command! Sir!')

startExecution = mainT()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)


    def startTask(self):
        self.ui.movie = QtGui.QMovie("E:\jarvis1\lib\ironman.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:\jarvis1\lib\initial.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
        
