import cv2

def draw_creeper(frame,x,y,w,h):
    cv2.rectangle(frame, (x, y), (x + w, y + h), (34, 139, 34), -2)                                                                      #draw face
    cv2.rectangle(frame, (x + int(w / 3) - 20, y + int(h / 3) - 10), (x + int(w / 3) + 5, y + int(h / 3) + 10), (0, 0, 0), -2)           #draw left eye
    cv2.rectangle(frame, (x + 2 * int(w / 3) - 15, y + int(h / 3) - 10), (x + 2 * int(w / 3) + 10, y + int(h / 3) + 10), (0, 0, 0), -2)  #draw right eye
    cv2.rectangle(frame, (x + int(w / 3) + 5, y + int(h / 3) + 10), (x + 2 * int(w / 3) - 15, y + int(h / 3) + 30), (0, 0, 0), -2)       #draw nose
    cv2.rectangle(frame, (x + int(w / 3) - 10, y + int(h / 3) + 30), (x + 2 * int(w / 3), y + int(h / 3) + 60), (0, 0, 0), -2)           #the rest draw mouth
    cv2.rectangle(frame, (x + int(w / 3) - 10, y + int(h / 3) + 60), (x + int(w / 3) + 5, y + int(h / 3) + 73), (0, 0, 0), -2)
    cv2.rectangle(frame, (x + 2 * int(w / 3) - 15, y + int(h / 3) + 60), (x + 2 * int(w / 3), y + int(h / 3) + 73), (0, 0, 0), -2)
