import numpy as np
import cv2 as cv


# Filter values got from 'background_capture.py'
ilowH = 150
ihighH = 179
ilowS = 150
ihighS = 255
ilowV = 95
ihighV = 255

hue_lower = 12

cap = cv.VideoCapture(0) # Change if you have more than 1 Cam input

cv.namedWindow('MainWindow', cv.WINDOW_AUTOSIZE)

background = 0

# Get Background Image
for i in range(20):
    ret, background = cap.read()

while cap.isOpened:
    
    ret, frame=cap.read()

    # Convert the image to HSV Colorspace
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)    

    # Filter Upper Red
    lower_red = np.array([ilowH,ilowS,ilowV])
    upper_red = np.array([ihighH,ihighS,ihighV])
    mask1 = cv.inRange(hsv,lower_red,upper_red)   

    # Filter Lower Red
    lower_red = np.array([0,ilowS,ilowV])
    upper_red = np.array([hue_lower,ihighS,ihighV])
    mask2 = cv.inRange(hsv, lower_red, upper_red)

    # Mix the filters
    mask1 = mask1 + mask2
    
    # remove the color from image
    mask1 = cv.morphologyEx(mask1, cv.MORPH_OPEN, np.ones((5,5),np.uint8))   
    mask2 = cv.bitwise_not(mask1)
    
    res1 = cv.bitwise_and(frame,frame,mask=mask2)
    res2 = cv.bitwise_and(background, background, mask = mask1)

    # mix the first frames into the masked
    final_output = cv.addWeighted(res1,1,res2,1,0)
    
    cv.imshow('MainWindow', final_output)

    key = cv.waitKey(10) & 0xFF

    if key == 113 or key == 27:
        break

cap.release()
cv.destroyAllWindows()
