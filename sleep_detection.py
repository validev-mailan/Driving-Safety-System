import cv2
import mediapipe as mp
import time
import math
import winsound

print("Running...")

# MediaPipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

mp_drawing = mp.solutions.drawing_utils

# Eye landmark indexes
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

# Function to calculate Eye Aspect Ratio (EAR)
def calculate_ear(eye):
    A = math.dist(eye[1], eye[5])
    B = math.dist(eye[2], eye[4])
    C = math.dist(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Camera
cap = cv2.VideoCapture(0)

EYE_AR_THRESHOLD = 0.25
SLEEP_TIME = 2  # seconds
counter = 0
alarm_on = False
start_time = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            left_eye = []
            right_eye = []

            for idx in LEFT_EYE:
                x = int(face_landmarks.landmark[idx].x * w)
                y = int(face_landmarks.landmark[idx].y * h)
                left_eye.append((x, y))

            for idx in RIGHT_EYE:
                x = int(face_landmarks.landmark[idx].x * w)
                y = int(face_landmarks.landmark[idx].y * h)
                right_eye.append((x, y))

            left_ear = calculate_ear(left_eye)
            right_ear = calculate_ear(right_eye)

            ear = (left_ear + right_ear) / 2.0

            # Draw eye points
            for point in left_eye + right_eye:
                cv2.circle(frame, point, 2, (0, 255, 0), -1)

            # Check sleep condition
            if ear < EYE_AR_THRESHOLD:
                if start_time is None:
                    start_time = time.time()
                else:
                    elapsed = time.time() - start_time

                    if elapsed >= SLEEP_TIME:
                        cv2.putText(frame, "SLEEPING!", (50, 100),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

                        # Alarm sound
                        winsound.Beep(1000, 500)

            else:
                start_time = None

            cv2.putText(frame, f"EAR: {ear:.2f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.imshow("Driver Sleep Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()