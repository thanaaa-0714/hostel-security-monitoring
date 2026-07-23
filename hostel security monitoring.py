from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    person_count = 0

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])

            # Detect only persons
            if cls == 0:
                person_count += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, "Person", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                            (0, 255, 0), 2)

    # Show total person count
    cv2.putText(frame, f"Persons: {person_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 0, 0), 2)

    cv2.imshow("AI Hostel Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
 

