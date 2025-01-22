from ultralytics import YOLO
import cv2
import math

model = YOLO("yolo-Weights/yolov5m.pt")

results = model.train(
    data = "datasets\data.yaml",
    epochs = 10,
    imgsz = 640
)