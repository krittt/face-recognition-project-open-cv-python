# face-recognition attendance project by open-cv and python/
 this is an open cv project using some python libraries for the face recognition attendance system.
 which recognizes the face once and puts an attendance is the .csv file 
 
 you are required to import the following libraries to your local machine via (pip install {name of the lib}) command on the CMD
 *import cv2
 *import csv
 *import path from importlib.resources
 *import datetime from datetime  #for the attendance marksheet#
 *import face_recognition  #module based on dlib where dlib encodes face in 128 different features#
                           #i.e. 128 different points from the face are encoded thats why ur face is considered unique of all#
 *import frame from tkinter
 *import os #to read images#
 *import numpy #used for working with arrays#
 
 in the first line of code the path of the code is given with a directory named images
 next an empty list of images and print the list of people to see if the images the read correctly or not 
 and split the name of the images with the extension. so that only the name of the file is shown without its extension
 
 # for face encryptings or face encodings
  make a different fuction with any suitable name accompained by an empty list
  and change the bgr format of the image to rgb for the os module to read it
  and return thd encoded list because without it no face distance or comparison v=could take place
  when all the encodings are complete . it will show a message of complete
  
  # for attendance record
  for recording attendance of the person a different fuction has to be made
  with file handling in python, writing to a .csv file to record the name, date and time of the person
  and split the string into a list item where each list is a list item seperated by a comma
  if name is not in the list and the code is required to copy the name, date and time for the person in the camera and enter the required details in the field
  *videocapture is 0 for the camera used by the laptop and 1 for the external camera
  
 # for an infinite loop
 here cam frame and a variable are provided 
 the images are resized and turned from bgr to rgb format for the os module to read it 
 then comparison of the face and face distance is recorded by returning the inc=dices of the min value along the axis
 if it matches the above requirements then the rectangle of the image with a given thickness and color along with the name is shown along with the text string of the image
 # and the attendance fuction is called here 
 
 cv2.imshow() *shows the image*
 waitkey()  *watiting for miliseconds to respond*
 break *breaking of the fuction*
 .release() *releasing the lock earlier acquired by a thread*
 cv2.destroyAllWindows *to destroy all windows at any time*
 
 # END OF THE CODE
 
 
 
  
  
  
 
 
 
 
 
 
 

 
 
 






