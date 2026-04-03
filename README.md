🚗 Driving Safety System (Drowsy Driver Detection)

📌 Overview

The Driving Safety System is a real-time computer vision-based project designed to detect driver drowsiness and prevent accidents.
It continuously monitors the driver’s eyes using a webcam and triggers alerts when signs of sleepiness are detected.

In addition, the system sends an emergency SMS alert with location details using the Twilio API, ensuring immediate response in critical situations.

---

🎯 Purpose

- To reduce road accidents caused by driver fatigue
- To provide real-time alert mechanisms for safety
- To notify emergency contacts using SMS alerts
- To build a smart and practical AI-based safety system

---

🚀 Features

- 😴 Real-time drowsiness detection using Eye Aspect Ratio (EAR)
- 🔊 Alarm sound alert when eyes remain closed
- 📱 Sends SMS alert using Twilio API
- 🌍 Shares live location via Google Maps link
- 🎥 Live video processing using OpenCV
- ⚡ Fast and efficient performance

---

🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- Twilio API
- Playsound

---

⚙️ How It Works

1. Webcam captures live video of the driver
2. Face and eye landmarks are detected
3. Eye Aspect Ratio (EAR) is calculated
4. If EAR falls below a threshold:
   - Alarm sound is triggered 🔊
   - SMS alert is sent 📱
5. Location is shared via Google Maps link

---

▶️ How to Run

1. Clone the repository:

git clone https://github.com/your-username/Driving-Safety-System.git

2. Install required libraries:

pip install -r requirements.txt

3. Add your Twilio credentials in the code:

account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"
twilio_number = "YOUR_TWILIO_NUMBER"
my_number = "YOUR_PHONE_NUMBER"

4. Run the project:

python main.py

---

📂 Project Structure

- "main.py" → Main execution file
- "sleep_detection.py" → Drowsiness detection logic
- "drive mainpro.py" → Integrated system with alert + SMS
- "alarm.mp3" → Alarm sound file
- "README.md" → Project documentation

---

📸 Output

- Detects eye closure in real time
- Alerts driver with alarm sound
- Sends SMS notification with location

---

🔮 Future Enhancements

- Mobile app integration for alerts
- AI model improvement using deep learning
- Driver performance tracking system
- Integration with vehicle systems

---

⚠️ Security Note

Do not upload your real Twilio Account SID and Auth Token to GitHub.
Always keep your credentials secure.

---

👨‍💻 Author

DHANALAKSHMI
