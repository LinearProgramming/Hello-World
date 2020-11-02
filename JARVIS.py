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

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('VSD547-VGHE57128')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)

def speak(audio):
    print('JARVIS: ' + audio)
    engine.say(audio)
    engine.runAndWait()
    
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if currentH >= 0 and currentH < 12:
        speak(f'Good Morning Sir, its {tt}')

    elif currentH >= 12 and currentH < 18:
        speak(f'Good Afternoon Sir, its {tt}')

    else: 
        speak(f'Good Evening Sir, its {tt}')

greetMe()

speak('Hello Sir, I am  JARVIS!')
speak('What can I do for you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('SIR: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry Sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay Sir')
            webbrowser.open('www.youtube.com')

        elif 'open notepad' in query:
            speak('okay sir, opening notepad')
            subprocess.call(r'C:\\Windows\\system32\\notepad.exe')

        elif 'open google' in query:
            speak('okay Sir,opening Google')
            cm = takecommand().lower()
            webbrowser.open('www.google.co.in')

        elif 'open my github id' in query:
            speak('okay Sir, opening your GITHUB id')
            webbrowser.open('https://github.com/LinearProgramming/Hello-World')

        elif 'open gmail' in query:
            speak('okay Sir, opening gmail')
            webbrowser.open('www.gmail.com')
       
        elif 'open powerpoint' in query:
            speak('okay boss, opening powerpoint')
            subprocess.call(r'C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.EXE')    

        elif 'open winword' in query:
            speak('okay Sir, opening winword')
            subprocess.call(r'C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.EXE')

        elif 'open excel' in query:
            speak('okay Sir, opening excel')
            subprocess.call(r'C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.EXE')    

        elif 'open obs studio' in query:
            speak('okay Sir, opening obs studio')
            subprocess.call(r'E:\\screen recorder\\obs-studio\\bin\\64bit\\obs64.exe')

        elif 'open iron man' in query:
            speak('okay Sir, opening iron man')
            subprocess.call(r'E:\\Iron Man 2008 PC Game\\GameLauncher.exe')

        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'detect face' in query:
            speak('okay Sir! runing face detection mode')
            #for getting a reference from webcam
            video_capture = cv2.VideoCapture(0)


            #load some images you want to recognise
            
            Abhimanyu_image = face_recognition.load_image_file("Abhimanyu.jpg")
            Abhimanyu_face_encoding = face_recognition.face_encodings(Abhimanyu_image)[0]

            Abhinav_image = face_recognition.load_image_file("Abhinav.jpg")
            Abhinav_face_encoding = face_recognition.face_encodings(Abhinav_image)[0]

            #create arrays of known_face_encodings & names
            known_face_encodings = [
                Abhimanyu_face_encoding,
                Abhinav_face_encoding
            ]

            known_face_names = [
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

        
        elif 'shutdown' in query:
            speak('okay Sir, work in progress')
            os.system('shutdown -s')

        elif 'tell me joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = 'E:\song\Bulleya.mp3'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'restart' in query:
            speak('okay Sir, work in progress')
            os.system('shutdown /r /t 5')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Boss! I am unable to send your message at this moment!')

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay Sir')
            speak('Bye Sir,have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'are you here' in query:
            speak('Yes Sir, I am always here for you boss')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
          
        elif 'play music' in query:
            music_folder = 'E:\song/'
            music = ['Dil_Mein_Mars_Hai_-_Mission_Mangal__Akshay__Vidya__Sonakshi__Taapsee__Benny_Dayal_&_Vibha_Saraf(128kbps)', 'Baaki_Baatein_Peene_Baad_-_Arjun_Kanungo_feat._Badshah___Nikke_Nikke_Shots__', 'Jab_Tak', 'Besabriyaan', 'Daru_party', 'Kaun_Tujhe', 'Main_Hoon', 'Daspacito_Justin_Bieber_Luis_Fonsi', 'Commando_2__Hare_Krishna_Hare_Ram___Vidyut_Jammwal,_Adah_Sharma,_Esha_Gupta,', 'Imran_Khan_-_Satisfya_(Official_Music_Video)(128kbps)', 'Ik_Vaari_Aa___Raabta___Sushant_Singh_Rajput___Kriti_Sanon___Pritam_Arijit_Singh_', 'Ding_Dang_-_Full_song_with_lyrics__7C_Munna_Michael_2017__7C_Tiger_Shroff__26_Nidhhi_A', 'Feel_The_Rhythm_-_Full_Audio_Song__7C_Munna_Michael__7C_Tiger_Shroff__26_Nidhhi_Agerwa', 'Moto_(Official_Video)_Ajay_Hooda__Diler_Kharkiya__Anjali_Raghav__Latest_Haryanvi_Song_2020(128kbps)']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            speak('Okay Sir, here is your music! Enjoy!')
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')

