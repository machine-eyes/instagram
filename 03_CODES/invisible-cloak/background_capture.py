import numpy as np
import cv2 as cv


def callback(x):
    pass

ilowH = 0
ihighH = 179
ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

cap = cv.VideoCapture(0)

cv.namedWindow('MainWindow', cv.WINDOW_AUTOSIZE)

# create trackbars for color change
cv.createTrackbar('lowH', 'MainWindow', ilowH, 179, callback)
cv.createTrackbar('highH', 'MainWindow', ihighH, 179, callback)
cv.createTrackbar('lowS', 'MainWindow', ilowS, 255, callback)
cv.createTrackbar('highS', 'MainWindow', ihighS, 255, callback)

cv.createTrackbar('lowV', 'MainWindow', ilowV, 255, callback)
cv.createTrackbar('highV', 'MainWindow', ihighV, 255, callback)

cv.namedWindow('MainWindow', cv.WINDOW_AUTOSIZE)

while cap.isOpened:
    # grab the frame
    ret, frame = cap.read()

    # get trackbar positions
    ilowH = cv.getTrackbarPos('lowH', 'MainWindow')
    ihighH = cv.getTrackbarPos('highH', 'MainWindow')
    ilowS = cv.getTrackbarPos('lowS', 'MainWindow')
    ihighS = cv.getTrackbarPos('highS', 'MainWindow')
    ilowV = cv.getTrackbarPos('lowV', 'MainWindow')
    ihighV = cv.getTrackbarPos('highV', 'MainWindow')

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    mask = cv.inRange(hsv, lower_hsv, higher_hsv)

    frame = cv.bitwise_and(frame, frame, mask=mask)

    # show thresholded image
    cv.imshow('MainWindow', frame)
    key = cv.waitKey(100) & 0xFF  # large wait time to remove freezing
    if key == 113 or key == 27:
        break

cap.release()
cv.destroyAllWindows()

