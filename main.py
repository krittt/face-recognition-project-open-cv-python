import cv2
import csv
from importlib.resources import path
from datetime import datetime   #for the attendance marksheet
import face_recognition   #module based on dlib where dlib encodes face in 128 different features
#i.e. 128 different points from the face are encoded thats why ur face is considered unique of all
import numpy as np
from tkinter import Frame
import os   # os module to read images

path = 'images'  #directory name
images = []  #empty list of images
nameofpeople = []
mylistofpeople = os.listdir(path)  #used to get the list of all files and directories in the specified directory
print(mylistofpeople)  #to see if the images are read inside the directory
for ongoingimage in mylistofpeople:
    currentimage = cv2.imread(f'{path}/{ongoingimage}')  #cv2.imread to read images
    images.append(currentimage) #to add the current image visible in the empty images list
    nameofpeople.append(os.path.splitext(ongoingimage)[0])  #to split the name and the extention of the name image
print("\n")
print(nameofpeople)


def faceEncrypting(images):  #to find out the encoding of images using face-recognition
    encryptList = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  #bgr format to rgb
        code = face_recognition.face_encodings(image)[0]  #images ka first element 0th element
        encryptList.append(code)
    return encryptList  #without this no face comparison or face distance could be found out

encryptknownlist = faceEncrypting(images) 
print("\n All of the grablings are complete.. ")

#function for attendance through file handling in python
def attendanceofpeople(name):
    with open('attend.csv', 'r+') as g:
        myunitlist = g.readlines()   #to read the lines of the .csv file 
        namelist = []   #empty namelist 
        for unit in myunitlist:
            entry = unit.split(',')   #Split a string into a list where each word is a list item
            namelist.append(entry[0])  #add at the 0th element of the list
        if name not in namelist:
            atpresnt = datetime.now()  #to get the present date and time
            date = atpresnt.strftime('%d/%m/%Y')  #day month year
            time = atpresnt.strftime('%H:%M:%S')  #hrs min sec
            g.writelines(f'\n{name}, {date}, {time}')
        

warsaw = cv2.VideoCapture(0)

while True:  #infinite loop
    retard, encase = warsaw.read()   #returns camera frame and ret variable
    faces = cv2.resize(encase, (0,0), None, 0.25, 0.25)   #resize the values , destinantion, fx fy 1/4th=0.25
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)   #again input of faces is converted to rgb

    facespresentframe = face_recognition.face_locations(faces)  #finds faces in the current frame faces
    encodespresentframe = face_recognition.face_encodings(faces, facespresentframe)  
    #for encodings we need both current face and camera 
    
    #The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
    for encodeFace, Facelocation in zip(encodespresentframe, facespresentframe):
        matches = face_recognition.compare_faces(encryptknownlist, encodeFace)  #compares the face
        facegap = face_recognition.face_distance(encryptknownlist, encodeFace)  #evaluates the distance between the face and the screen/cam

        complementindex = np.argmin(facegap) #Returns the indices of the minimum values along an axis

        if matches[complementindex]:
            name = nameofpeople[complementindex].upper()  #uppercase
            y1,x2,y2,x1 = Facelocation
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4

            #syntax: cv2.rectangle(image, start_point, end_point, color, thickness)
            #cv2.rectangle() : method is used to draw a rectangle on any image
            cv2.rectangle(encase, (x1,y1), (x2,y2), (0,100,0), 3)
            cv2.rectangle(encase, (x1, y2-35), (x2,y2),(0,100,0), cv2.FILLED)
            cv2.putText(encase, name, (x1+4, y2-4), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)   #used to draw a text string on any image
            attendanceofpeople(name)    #calling the function


    cv2.imshow("Camera", encase)   #showing the image
    if cv2.waitKey(20) == 13:   #waiting using waitkey method
        break  #breaks the line or function

warsaw.release()  #releases the lock which was earlier acquired by a thread
cv2.destroyAllWindows()   #destroy all windows at any time without any parameters taken










