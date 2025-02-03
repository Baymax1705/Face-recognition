import cv2 as cv
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')  ## Load the pre-trained Haar cascade for face detection

webcam=cv.VideoCapture(0)  #opening the webcam
if not webcam.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret,frames=webcam.read()  #gives two values 1. boolean value 2. frame
    if not ret:
        print("Error: Failed to capture frame.")
        continue
    gray=cv.cvtColor(frames,cv.COLOR_BGR2GRAY)  #converting the frame to grayscale for better detection

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)   #@scale@Lower values(~1.1 - 1.3): More detections but slower|||.Higher values (>1.5): Faster, but may miss smaller faces.
                                                                     # @min##Higher values (>4): Fewer but more accurate detections.Lower values (<3): More detections, but more false positives.
    for (x,y,w,h) in faces:      #x,y->top left corner of the face  w->width of the face  h->height of the face
        cv.rectangle(frames,(x,y),(x+w,y+h),(0,255,0),2)  #drawing a rectangle around the face

    cv.imshow('WEBCAM',frames)
    if cv.waitKey(10) & 0xFF==ord('d'):
        break

       #if 27==key -> 27 is the ASCII value of the ESC key
       # key=cv.waitKey(10)       OR   key=cv.waitKey(10) & 0xFF==27
        # if key==27:
        #     break

webcam.release()  #releasing the webcam
cv.destroyAllWindows()  #closing all the windows
