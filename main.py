import cv2
from ultralytics import YOLO
import pyttsx3

# 1. Initialize the Brain (YOLOv8-Nano)
model = YOLO('yolov8n.pt')

# 2. Initialize the Voice & Adjust Settings for Clarity
engine = pyttsx3.init()
engine.setProperty('rate', 160) 
engine.setProperty('volume', 1.0)  

# 3. Setup the Webcam
cap = cv2.VideoCapture(0)

print("Vision Assistant Active. Press 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model(frame, conf=0.6, iou=0.5)

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]
            confidence = float(box.conf[0])

            useful_objects = ['smart phone', 'bottle', 'remote', 'chair', 'cup', 'watch', 'person']
            
            if label in useful_objects:
                print(f"I see a {label} ({confidence:.2f} confidence)")
                
                if confidence > 0.65:
                    engine.say(f"I see a {label}")
                    engine.runAndWait()


    annotated_frame = results[0].plot()
    cv2.imshow("AI Vision Assistant", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
