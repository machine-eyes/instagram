import cv2 as cv
from time import sleep

cap = cv.VideoCapture(0)

sleep(3)

_, frame = cap.read()

while True:

    _, frame = cap.read()

    lab = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsl = cv.cvtColor(frame, cv.COLOR_BGR2HLS)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    grb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    # a = cv.cvtColor(frame, cv.COLOR_BGR2LUV)

    

    cv.imshow('Main', frame)
    cv.imshow('HSV', hsv)
    cv.imshow('HSL', hsl)
    cv.imshow('Lab', lab)
    cv.imshow('GRB', grb)
    cv.imshow('Gray', gray)

    key = cv.waitKey(10)
    if key == ord('q') & 0xFF:
        break

cap.release()
cv.destroyAllWindows()