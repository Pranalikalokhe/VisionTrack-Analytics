from ultralytics import YOLO
import cv2

# Load YOLO model once
model = YOLO("yolov8n.pt")

# COCO class IDs
PERSON_CLASS = 0
VEHICLE_CLASSES = [2, 3, 5, 7]  # car, motorcycle, bus, truck
ANIMAL_CLASSES = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23] # bird, cat, dog, horse, etc.
STREET_CLASSES = [9, 10, 11] # traffic light, fire hydrant, stop sign

def detect_frame(frame):
    # Resize small images so bounding boxes don't get drawn too thick
    h, w = frame.shape[:2]
    if w < 800:
        scale = 800 / w
        frame = cv2.resize(frame, (int(w * scale), int(h * scale)))

    results = model(frame)
    boxes = results[0].boxes

    counts = {
        "people": 0,
        "vehicles": 0,
        "animals": 0,
        "street_objects": 0
    }

    for box in boxes:
        cls = int(box.cls[0])

        if cls == PERSON_CLASS:
            counts["people"] += 1
        elif cls in VEHICLE_CLASSES:
            counts["vehicles"] += 1
        elif cls in ANIMAL_CLASSES:
            counts["animals"] += 1
        elif cls in STREET_CLASSES:
            counts["street_objects"] += 1

    annotated = results[0].plot()

    return annotated, counts