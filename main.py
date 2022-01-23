# Import statements
import cv2
import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier("Classifiers/haarcascade_frontalface_alt.xml")
eye_cascade = cv.CascadeClassifier("Classifiers/haarcascade_eye_tree_eyeglasses.xml")

img = cv.imread("Images/Ace.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img)

for (x, y, w, h) in faces:
    face_center = (x + w//2, y + h//2)
    img = cv.ellipse(img, face_center, (w//2, h//2), 0, 0, 360, (255, 0, 0), 2)
    roi_gray = gray_img[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)

    for (x1, y1, w1, h1) in eyes:
        cv.rectangle(roi_color, (x1, y1), (x1+w1, y1+h1), (0,255,0), 2)
    cv.imshow('ROCK', img)

cv.waitKey(0)
cv.destroyAllWindows()
