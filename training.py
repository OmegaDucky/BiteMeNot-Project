# Training Code
from ultralytics import YOLO

model = YOLO("/tmp/yolov8n.pt")

results = model.train(
    data="/content/data.yaml",
    epochs=40,
    imgsz=640
)

val1 = model.val()
