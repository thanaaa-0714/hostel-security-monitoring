import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

def scan_person():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                # Person class
                if cls == 0:

                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    cv2.rectangle(frame,
                                  (x1, y1),
                                  (x2, y2),
                                  (0, 255, 0),
                                  2)

                    cv2.putText(frame,
                                "Person Detected",
                                (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.8,
                                (0,255,0),
                                2)

        cv2.imshow("Hostel Security Monitoring", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_person()