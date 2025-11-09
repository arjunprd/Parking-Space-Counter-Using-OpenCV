import cv2
import pickle
import os

rectW, rectH = 107, 48

# Automatically detect current script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define file paths relative to this directory
pos_file = os.path.join(BASE_DIR, 'carParkPos')
img_path = os.path.join(BASE_DIR, 'img.png')

# Load saved positions if they exist
if os.path.exists(pos_file):
    with open(pos_file, 'rb') as f:
        poslist = pickle.load(f)
else:
    poslist = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        poslist.append((x, y))
    elif events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(poslist):
            x1, y1 = pos
            if x1 < x < x1 + rectW and y1 < y < y1 + rectH:
                poslist.pop(i)
    with open(pos_file, 'wb') as f:
        pickle.dump(poslist, f)

# Load image for marking
img = cv2.imread(img_path)
if img is None:
    print(f"❌ Could not load image at: {img_path}")
    exit()

while True:
    img_copy = img.copy()
    for pos in poslist:
        cv2.rectangle(img_copy, pos, (pos[0] + rectW, pos[1] + rectH), (0, 0, 255), 2)
    cv2.imshow("Image", img_copy)
    cv2.setMouseCallback("Image", mouseClick)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cv2.destroyAllWindows()
