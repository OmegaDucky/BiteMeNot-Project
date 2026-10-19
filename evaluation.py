# Validation Correct Rate Code

from ultralytics import YOLO
# No need to import again if it has been done already

model = YOLO("/content/[yourmodelname].pt") # the model broski

metrics = model.val()
print(metrics.box.map)  # Prints mAP50-95, allowing evaluation
