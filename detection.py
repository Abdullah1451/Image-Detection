from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))#using ML model 'resnet50_coco_best_v2.0.1.h5' to detect all object and persons
detector.loadModel()

detections = detector.detectObjectsFromImage(
    input_image=os.path.join(execution_path, "image.jpg"),
    output_image_path=os.path.join(execution_path, "WOW-NEW-CAT-DETECTION-IMAGE.jpg"),
    minimum_percentage_probability=50,
)

for eachObject in detections:
    print(eachObject["name"], ": ", eachObject["percentage_probability"])
