import cv2
import numpy


# Load the pre-trained model to identify faces from opencv
trained_face_data=cv2.cascadeclassifier("haarcascade_frontalface_default.xml")

#Load the pre-trained model to identify smiles from open cv
smile_data=cv2.cascadeclassifier("haarcascade_smile.xml")

#Use webcam video

webcam=cv2.VideoCapture(0)

#To continously capture the video from webcam

while True:
    #Read the current frame from webcam. 
    sucessful_frame_read, frame=webcam.read()

    #To abort in case the webcam is not capturing a video
    if not sucess_frame_read:
        break

    #Change video to grayscale. This is because the haarcascade is based on the value, so the color information is not needed
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Detect faces. Since smiles only happen in faces, this is done to make sure the smiles detected are truly smiles on human faces
    faces=trained_face_data.detectMultiScale(frame_gray)

    #To restrict the smile detector to faces
    for (x,y,w,h) in faces:
        #Drawing a green rectangle around the face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)

        #Face coordinates
        the_face=frame[y:y+h, x:x+w]

        #Converting the face to grayscale

        the_face_gray=cv2.cvtColor(the_face,cv2.COLOR_BGR2GRAY)
         #detect smiles. The scale factor and minimum neighbors were determined through trial and error
        smiles= smile_data.detectMultiScale(the_face_gray, scaleFactor=1.7, MinNeighbors=20)

        #Label the face as smiling

        if len(smile)>0:
            cv2.putText(frame, 'smile', (x, y+h+40), fontScale=3, fontFace=cv2.FONT_HERSHEY_PLAIN, color =(255,0,0))
    #Show the frame with the smile and face detector
    cv2.imshow("Smile Detector", frame)

    #Skip to the next frame every 1 ms

    key=cv2.waitKey(1)

    #To quit the program by pressing q or Q
    if key==81 or key ==113:
	break
#To let go of the webcam and save memory
webcam.release()
cv2.destroyAllWindows()



    

    

        

   

    

