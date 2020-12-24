import cv2
import os
import sys
from datetime import datetime
from time import sleep

# capture and save
def main():
    cap = cv2.VideoCapture(0)
    sleep(1)
    ret, frame = cap.read()
    cv2.imwrite("test.jpg", frame)
    return 0

if __name__ == "__main__":
    main()

