import cv2
import numpy as np

def vid_proc(file):
    cap = cv2.VideoCapture(0)
    down_points = (640, 480)
    
    alpha = 0.9999

    while True:
        ret, frame = cap.read()
        frame1 = frame
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21,21), 0)
        ret, tresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)
        contours, hierarchy = cv2.findContours(tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contours) >0:
            c = max(contours, key=cv2.contourArea)
            x,y,w,h = cv2.boundingRect(c)
            file.write(f"{x+w//2}, {y+h//2} \n")
            #frame[(x+w//2-32):(x+w//2+32), (y+h//2-32):(y+h//2+32)] = frame[(x+w//2-32):(x+w//2+32), (y+h//2-32):(y+h//2+32)]*(1 - alpha) + alpha*fly
         #   frame[x:64+x, y:64+y, :] = fly[0:64, 0:64, :]

            #roi = frame[-size-8:-8, -size-8:-8]
        
            #roi[np.where(mask)] = 0
            #roi += fly
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("Contours", frame)
        if cv2.waitKey(1)&0xFF == ord("q"):
            break


with open("logs.txt", "+w") as file:
    vid_proc(file)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    file.close()
