
# 🔫 Smart Weapon Detection System using YOLOv8

This project is a real-time CCTV-based object detection system that identifies weapons (like guns or knives) using a deep learning model. It was built to simulate a security tool for public safety surveillance.

---

## 📌 Objective

To create a working computer vision system that detects dangerous objects in surveillance footage and helps raise alerts to prevent threats in sensitive areas.

---

## 🧠 Tech Stack

- Python 3.10
- OpenCV
- YOLOv8 (Ultralytics)
- VS Code
- Windows OS

---

## 📂 Folder Structure

```
weapon-detection-cctv/
├── detect_weapon.py           # Main detection script
├── yolov8_weights/            # YOLO model file here
│   └── yolov8n.pt
├── test_videos/               # Input video to test
│   └── sample_cctv_clip.mp4
├── outputs/                   # Detected frames saved here
│   └── detected_frames/
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/ayushpali/Weapon-Detection-CCTV.git
   cd weapon-detection-cctv
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download YOLOv8 weights:
   ```python
   from ultralytics import YOLO
   YOLO("yolov8n.pt")
   ```
   Move the file to `yolov8_weights/`

5. Run the script:
   ```bash
   python detect_weapon.py
   ```

Press **Q** to quit the video preview.

---

## 📷 Sample Output

(outputs/detected_frames/frame_0.jpg)


---

## 📌 Future Ideas

- Filter output to show only weapons (e.g., guns/knives)
- Send alerts via SMS or Email using Twilio
- Add a Streamlit dashboard to control detection and logs

---

## 🙋 Author

**Ayush Pali**  
[GitHub](https://github.com/ayushpali/Weapon-Detection-CCTV)

---
