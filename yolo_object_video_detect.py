import cv2
import numpy as np
import glob
import random


# Load Yolo
net = cv2.dnn.readNet("yolov3_training_final.weights", "yolov3_testing.cfg")

# Name custom object
classes = ["Dr_Pepper"]

# Images path
File = "Test.jpg"
images_path = glob.glob(r"D:\\Deep_Learning\\Task\\" + File)
filename = "Output_New"+File



layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Insert here the path of your images
random.shuffle(images_path)


def detect_image(frame):
    # loop through all the images
    # for img_path in images_path:
    # Loading image
    # img = cv2.imread(img_path)
    img = cv2.resize(frame, None, fx=0.7, fy=0.7)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3:
                # Object detected
                print(class_id)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    print(indexes)
    print(len(indexes))
    
    font = cv2.FONT_HERSHEY_PLAIN
    font_scale = 0.6
    text = "Total no. of detections = {}".format(len(indexes))
    (text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=1)[0]
    text_offset_x = 7
    text_offset_y = 25
    box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width + 2, text_offset_y - text_height - 2))
    # cv2.rectangle(img, box_coords[0], box_coords[1], (255,255,255), cv2.FILLED)
    cv2.putText(img, text, (text_offset_x, text_offset_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0), 2)
    # cv2.putText(img, label, (x, y + 30), font, 1, (0,0,0), 1)
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,0), 2)
            cv2.putText(img, label, (x, y + 30), font, 1, (0,255,0), 1)
            # cv2.imwrite(filename, img)
    return img

vid = cv2.VideoCapture(0)
if not vid.isOpened():
    raise IOError("Couldn't open webcam or video")


while True:
    cv2.waitKey(10)
    return_value, frame = vid.read()
    frame = detect_image(frame)
    cv2.imshow("result", frame)

cv2.destroyAllWindows()