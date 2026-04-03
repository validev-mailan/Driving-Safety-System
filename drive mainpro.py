import cv2
import time
from playsound import playsound
from twilio.rest import Client
import mediapipe as mp

# -------- TWILIO CONFIG --------
account_sid = "YOUR_SID_NUMBER"
auth_token = "YOUR_AUTH_NUMBER"

client = Client(account_sid, auth_token)

twilio_number = "YOUR_TWILIO_NUMBER"   # Twilio number
my_number = "YOUR_PHONE_NUMBER"      # Your number
location_link = "https://maps.google.com/?q=13.0827,80.2707"

# -------- MEDIAPIPE SETUP --------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# -------- CAMERA --------
cap = cv2.VideoCapture(0)

# -------- EYE LANDMARKS --------
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

# -------- FUNCTION --------
def calculate_ear(landmarks, eye_points, w, h):
    pts = [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in eye_points]

    A = ((pts[1][0] - pts[5][0])**2 + (pts[1][1] - pts[5][1])**2) ** 0.5
    B = ((pts[2][0] - pts[4][0])**2 + (pts[2][1] - pts[4][1])**2) ** 0.5
    C = ((pts[0][0] - pts[3][0])**2 + (pts[0][1] - pts[3][1])**2) ** 0.5

    ear = (A + B) / (2.0 * C)
    return ear

# -------- VARIABLES --------
start_time = None
ALARM_THRESHOLD = 0.25   # eye closed threshold
CLOSED_TIME_LIMIT = 2    # seconds

# -------- LOOP --------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:

            left_ear = calculate_ear(face_landmarks.landmark, LEFT_EYE, w, h)
            right_ear = calculate_ear(face_landmarks.landmark, RIGHT_EYE, w, h)

            ear = (left_ear + right_ear) / 2.0

            if ear < ALARM_THRESHOLD:
                if start_time is None:
                    start_time = time.time()
                else:
                    duration = time.time() - start_time

                    if duration > CLOSED_TIME_LIMIT:
                       print("🚨 ALERT: Eyes closed!")

                       # ✅ FIRST SMS
                       try:
                         client.messages.create(
                            body="🚨 Eyes closed alert!Location:"
                          + location_link,
                            from_=twilio_number,
                            to=my_number
                         )
                         print("SMS Sent ✅")
                       except Exception as e:
                         print("SMS Error:", e)

                      # ✅ THEN alarm
                       playsound("alarm.mp3")

                       start_time = None

    cv2.imshow("Face + Eye Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cap.release()
cv2.destroyAllWindows()