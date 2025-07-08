import cv2
from ultralytics import YOLO
import os

import smtplib
from email.message import EmailMessage

def send_email_alert(frame_path):
    EMAIL_ADDRESS = "yourgmail@gmail.com"             # your Gmail address
    EMAIL_PASSWORD = "your-16-char-app-password"         # the 16-character app password

    msg = EmailMessage()
    msg["Subject"] = "🚨 Weapon Detected!"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = "recipient@example.com"
    msg.set_content("A weapon (Handgun) was detected. See the attached image.")

    with open(frame_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="image", subtype="jpeg", filename="detection.jpg")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("📧 Email alert sent!")





# Load trained YOLO model
model = YOLO("runs/detect/train6/weights/best.pt")

# Confirm class names
print("Model classes:", model.names)

# Create output folder if it doesn't exist
os.makedirs("outputs/detected_frames", exist_ok=True)

# Open video
cap = cv2.VideoCapture("test_videos/sample_cctv_clip.mp4")
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)
    annotated_frame = results[0].plot()

    # Detection filter: only save if "Handgun" detected
    detected = False
    for box in results[0].boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        print("Detected:", class_name)
        if class_name == "Handgun":  # exact match
            detected = True
            break

    if detected:
        filename = f"outputs/detected_frames/frame_{frame_count}.jpg"
        cv2.imwrite(filename, annotated_frame)
        print(f"✅ Saved: {filename}")
        send_email_alert(filename)

    # Show live preview
    cv2.imshow("Smart Weapon Detector", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    frame_count += 1

cap.release()
cv2.destroyAllWindows()
