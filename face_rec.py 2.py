#import libraries
import face_recognition
import cv2
import numpy as np

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
    cv2.imshow('LINEAR Face_Recognition',frame)

    #exit key for quit a program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
