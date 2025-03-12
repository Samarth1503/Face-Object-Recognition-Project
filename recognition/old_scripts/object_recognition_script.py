# import cv2
# import numpy as np

# # Load pre-trained model and class labels
# prototxt_path = "models/MobileNetSSD_deploy.prototxt"
# model_path = "models/mobilenet_iter_73000.caffemodel"
# net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# # List of class labels for the model
# CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle",
#            "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse",
#            "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

# # Detect objects in an image
# def detect_objects(image_path):
#     image = cv2.imread(image_path)
#     h, w = image.shape[:2]

#     # Convert image to blob for model processing
#     blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)
#     net.setInput(blob)
#     detections = net.forward()

#     for i in range(detections.shape[2]):
#         confidence = detections[0, 0, i, 2]

#         if confidence > 0.5:  # Filter weak detections
#             class_id = int(detections[0, 0, i, 1])
#             box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
#             (startX, startY, endX, endY) = box.astype("int")

#             label = f"{CLASSES[class_id]}: {confidence:.2f}"
#             cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
#             cv2.putText(image, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     cv2.imshow("Object Recognition", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# # Test Object Recognition
# if __name__ == "__main__":
#     detect_objects("data/objects/test.jpg")  # Replace with your image path



# With bottom prompt
# With bottom prompt
# With bottom prompt

# import cv2
# import numpy as np

# def main():
#     # Load pre-trained model and class labels
#     prototxt_path = "models/MobileNetSSD_deploy.prototxt"
#     model_path = "models/mobilenet_iter_73000.caffemodel"
#     net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

#     # List of class labels for the model
#     CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle",
#                "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse",
#                "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
    
#     cap = cv2.VideoCapture(0)
    
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
        
#         h, w = frame.shape[:2]
#         blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
#         net.setInput(blob)
#         detections = net.forward()
#         detected_label = "Detecting..."

#         for i in range(detections.shape[2]):
#             confidence = detections[0, 0, i, 2]
#             if confidence > 0.5:  # Filter weak detections
#                 class_id = int(detections[0, 0, i, 1])
#                 box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
#                 (startX, startY, endX, endY) = box.astype("int")
                
#                 label = f"{CLASSES[class_id]}: {confidence:.2f}"
#                 detected_label = CLASSES[class_id]  # Update detected label
                
#                 cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
#                 cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
#         # Display detected object name at bottom of frame
#         cv2.rectangle(frame, (0, h - 40), (w, h), (0, 0, 0), -1)  # Black rectangle background
#         cv2.putText(frame, detected_label, (10, h - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
#         cv2.imshow("Object Recognition", frame)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()




















# import cv2
# import numpy as np

# # Load pre-trained model and class labels
# prototxt_path = "models/MobileNetSSD_deploy.prototxt"
# model_path = "models/mobilenet_iter_73000.caffemodel"
# net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# # List of class labels for the model
# CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle",
#            "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse",
#            "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

# # Detect objects in an image
# def detect_objects(image_path):
#     image = cv2.imread(image_path)
#     h, w = image.shape[:2]

#     blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)
#     net.setInput(blob)
#     detections = net.forward()

#     num_detections = detections.shape[2]  # Number of detected objects
#     objects_detected = False  # Flag to track if any object is detected

#     for i in range(num_detections):
#         confidence = detections[0, 0, i, 2]

#         if confidence > 0.1:  # Adjusted confidence threshold
#             objects_detected = True  # Set the flag to True
#             class_id = int(detections[0, 0, i, 1])
#             box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
#             (startX, startY, endX, endY) = box.astype("int")

#             label = f"{CLASSES[class_id]}: {confidence:.2f}"
#             cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
#             cv2.putText(image, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#             # Display detected object name at bottom of frame
#             cv2.rectangle(image, (0, h - 40), (w, h), (0, 0, 0), -1)  # Black rectangle background
#             cv2.putText(image, label, (10, h - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#     if not objects_detected:  # If no objects were detected
#         cv2.rectangle(image, (0, h - 40), (w, h), (0, 0, 0), -1)  # Black background
#         cv2.putText(image, "Image not recognized", (10, h - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#     cv2.imshow("Object Recognition", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     detect_objects("data/objects/test_image.png")  # Replace with your image path







import cv2

config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

model = cv2.dnn_DetectionModel(frozen_model, config_file)

classLabels = []
filename = 'labels.txt'
with open(filename, 'rt') as spt:
    classLabels = spt.read().rstrip('\n').split('\n')
    
    
model.setInputSize(320, 320) #greater this value better the reults tune it for best output
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

    
img = cv2.imread('your image path')

classIndex, confidence, bbox = model.detect(img, confThreshold=0.5) #tune confThreshold for best results


font = cv2.FONT_HERSHEY_PLAIN

for classInd, conf, boxes in zip(classIndex.flatten(), confidence.flatten(), bbox):
    cv2.rectangle(img, boxes, (255, 0, 0), 2)
    cv2.putText(img, classLabels[classInd-1], (boxes[0] + 10, boxes[1] + 40), font, fontScale = 3, color=(0, 255, 0), thickness=3)
    
    
cv2.imshow('result', img)
cv2.waitKey(0)

cv2.imwrite('result.png', img)