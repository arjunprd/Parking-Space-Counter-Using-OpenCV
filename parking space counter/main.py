import cv2
import numpy as np
import pickle
import os

rectW, rectH = 107, 48

# Automatically detect current script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define file paths relative to this directory
video_path = os.path.join(BASE_DIR, 'carPark.mp4')
pos_file = os.path.join(BASE_DIR, 'carParkPos')

# Open video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"❌ Could not open video file at: {video_path}")
    exit()

# Load positions
if os.path.exists(pos_file):
    with open(pos_file, 'rb') as f:
        poslist = pickle.load(f)
else:
    print("⚠️ No 'carParkPos' file found. Run parking_space_picker.py first!")
    poslist = []

def check(imgPro):
    spaceCount = 0
    for pos in poslist:
        x, y = pos
        crop = imgPro[y:y + rectH, x:x + rectW]
        count = cv2.countNonZero(crop)
        if count < 900:
            spaceCount += 1
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)
        cv2.rectangle(img, pos, (x + rectW, y + rectH), color, 5)

    cv2.rectangle(img, (45, 30), (250, 75), (180, 0, 180), -1)
    cv2.putText(img, f'Free: {spaceCount}/{len(poslist)}', (50, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

while True:
    ret, img = cap.read()
    if not ret:
        print("⚠️ End of video or cannot read the frame.")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 1)
    thre = cv2.adaptiveThreshold(blur, 255,
                                 cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY_INV, 25, 16)
    blur = cv2.medianBlur(thre, 5)
    kernel = np.ones((3, 3), np.uint8)
    dilate = cv2.dilate(blur, kernel, iterations=1)
    check(dilate)

    cv2.imshow("Image", img)
    if cv2.waitKey(10) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()

 
