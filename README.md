# Driving-Safety-System
A smart driver safety system that detects drowsiness and sends real-time alerts with location to prevent accidents.
# 🚗 Drowsy Driving Safety System

## 📌 About
This project is a smart driver safety system designed to prevent accidents caused by driver drowsiness. It monitors the driver's face using a camera and detects sleep by analyzing eye closure.

If the driver closes their eyes for a few seconds, the system gives an alert sound. If the driver does not respond, it sends an emergency SMS alert to a predefined mobile number.

## 🚀 Features
- Real-time face detection
- Eye closure detection
- Instant alert sound
- Sends emergency SMS alert
- Works in low network conditions
- Suitable for long-distance drivers

## 🛠️ Technologies Used
- Python
- OpenCV
- NumPy

## ▶️ How it Works
1. Detects face using camera
2. Monitors eye movement
3. If eyes closed → alert sound
4. No response → send SMS alert

## 💡 Why SMS Instead of Email
SMS alerts are used instead of email because SMS works even with low network signal and does not require internet connection. This makes it more reliable for real-time emergency situations, especially for drivers traveling in remote areas.

## ▶️ How to Run
1. Install libraries:
   pip install opencv-python numpy

2. Run:
   python main.py

## 🙋‍♂️ Author
DHANALAKSHMI
