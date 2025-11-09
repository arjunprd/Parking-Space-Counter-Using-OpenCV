# Parking-Space-Counter-Using-OpenCV
# 🅿️ Parking Space Counter Using OpenCV

A computer vision project that automatically detects **available parking spaces** from a surveillance video feed.  
This system uses **OpenCV** to process video frames, detect empty spaces based on brightness thresholds, and display a live count of available spots.

---

## 📸 Overview

The project has two main parts:

1. **`parking_space_picker.py`** — A setup script where you manually mark parking spot positions using the mouse on a static reference image (usually a frame from the parking video).  
   - Left-click to **add** a parking spot  
   - Right-click to **remove** a parking spot  
   - Press **ESC** to exit and save positions  

2. **`main.py`** — The main detection script that processes each video frame and counts how many of the defined parking spaces are **free** or **occupied** in real-time.

---

## 🧩 Features

- 🧠 Automatic detection of empty vs occupied parking spots  
- 🖱️ Interactive spot selection (add/remove spots easily)  
- 🎥 Real-time frame-by-frame analysis  
- 💾 Persistent storage of parking spot data using Pickle  
- 🟩 Visual display of free/occupied spots on the video feed  

---



## 🗂️ Project Structure

Parking-Space-Counter-Using-OpenCV/
│
parking space counter/
    main.py # Main detection script
    parking_space_picker.py # Setup script to mark parking spots
    carPark.mp4 # Input video (parking lot footage)
    img.png # Static image used for marking (can be a frame from video)
    carParkPos # Pickle file storing parking spot coordinates
    README.md

---

## ⚙️ Requirements

Make sure you have **Python 3.7+** and install dependencies using:

```bash
pip install opencv-python numpy
```

🚀 Usage
Step 1: Prepare Your Project Folder

Place all of the following in the same directory:

**`main.py`**

**`parking_space_picker.py`**

**`carPark.mp4`** (your parking lot video)

**`img.png`** (a reference image — or use the video to create one)

💡 You can extract a frame from your video to use as img.png:

import cv2
cap = cv2.VideoCapture('carPark.mp4')
ret, frame = cap.read()
cv2.imwrite('img.png', frame)
cap.release()

Step 2: Mark Parking Spots

Run:

python parking_space_picker.py


Then:

Left-click on each parking spot to mark it

Right-click to remove a spot

Press ESC when done

This creates a carParkPos file (saved automatically) that stores your spot coordinates.

Step 3: Run the Parking Space Counter

Once your positions are marked, start the main script:

python main.py


This will:

Load your marked parking spaces

Analyze each frame of carPark.mp4

Display:

🟩 Green rectangles → free spaces

🟥 Red rectangles → occupied spaces

A live counter showing Free: X / Total

🧠 How It Works

Spot Selection
You select the coordinates of each parking space, which are saved using Python’s pickle module.

Frame Preprocessing
Each video frame is converted to grayscale, blurred, and thresholded to highlight occupied areas.

Binary Analysis
The algorithm crops each predefined parking rectangle and counts non-zero (white) pixels.

Low count → free space

High count → occupied space

Visualization
Each space is drawn as a colored rectangle on the live video feed, with real-time counts displayed.

🧱 Technical Details

Languages / Tools: Python, OpenCV, NumPy, Pickle

Key Functions Used:

cv2.VideoCapture() — for reading video frames

cv2.adaptiveThreshold() — for light-adaptive binarization

cv2.countNonZero() — to check occupancy

cv2.rectangle() & cv2.putText() — for drawing overlays

🧰 Troubleshooting
Problem	Possible Cause	Fix
FileNotFoundError: carParkPos	No saved positions	Run parking_space_picker.py first
cv2.error: !_src.empty()	Wrong video/image path	Files must be in the same folder as the script
No video displayed	Codec issue or wrong file format	Convert video to .mp4 or .avi
Window closes instantly	Press ESC to exit instead of closing manually	
🧩 Improvements (Future Work)

Integrate real-time camera feed instead of pre-recorded video

Add automatic spot detection using edge/contour detection

Implement a simple Flask dashboard to monitor parking status remotely

Log data (occupancy over time) for analytics

🏁 Credits

Developed by Arjun Prasad
Built with OpenCV and Python 3
