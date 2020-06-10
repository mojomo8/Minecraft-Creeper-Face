import cv2
from Draw_Face import draw_creeper
cascadePath = 'haarcascade_frontalface_default.xml' #replace with actual path to the haarcascade_frontalface_default.xml file
faceCascade = cv2.CascadeClassifier(cascadePath)

video_feed = cv2.VideoCapture(0)

while True:
    ret, frame = video_feed.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags= cv2.CASCADE_SCALE_IMAGE)

    # Draw the creeper over the face(s)
    for (x, y, w, h) in faces:
        draw_creeper(frame,x,y,w,h)

    # Display the frame wih Minecraft creeper face drawn
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  #NOTE: Press q to quit
        break

# Once ended, close video feed and window showing the frames
video_feed.release()
cv2.destroyAllWindows()