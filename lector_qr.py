import cv2
import numpy as np

capture = cv2.VideoCapture(0)


while(capture.isOpened()):
    ret, frame = capture.read()

    if(cv2.waitKey() == ord("s")):
        break
    qrDetector = cv2.QRCodeDetector()
    data, bbox, rectifiedImage = qrDetector.detectAndDecode(frame)

    if data:
        print(f"Dato: {data}")
        cv2.imshow('webcam',rectifiedImage)

    else:
        cv2.imshow('webcam', frame)

capture.release()
cv2.destroyAllWindows()
