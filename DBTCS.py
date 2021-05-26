import cv2
import numpy as np
from operator import itemgetter
from trafficlight import *

def ImgProcess(images):
    # Load Yolo
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Loading image
    img = cv2.imread(images)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
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
            if confidence > 0.6:
                # Object detected
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
    num4 = 0
    num41 = 0
    num42 = 0
    CarTotal = 0

    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 0.5, color, 0)
            

            # global num4
        
            num4 += label.count('car')
            num41 += label.count('truck')
            num42 += label.count('motorbike')

            CarTotal = num4 + num41 + num42

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return CarTotal


lane1 = ImgProcess("traff5.jpg")
lane2 = ImgProcess("traff4.jpg")
lane3 = ImgProcess("traff6.jpg")
lane4 = ImgProcess("em.jpeg")

total = lane1 + lane2 + lane3 + lane4

def time():
      global total, total_time, lane1_time, lane2_time, lane3_time, lane4_time 
      
      lane1_time = (lane1/total) * 60
      lane2_time = (lane2/total) * 60
      lane3_time = (lane3/total) * 60
      lane4_time = (lane4/total) * 60

      total_time = round(lane1_time) + round(lane2_time) + round(lane3_time) + round(lane4_time)

time()

def queue():

      list = [{'Lane': 1, 'No_of_Cars': lane1, 'Time' : round(lane1_time)},
              {'Lane': 2, 'No_of_Cars': lane2, 'Time' : round(lane2_time)},
              {'Lane': 3, 'No_of_Cars': lane3, 'Time' : round(lane3_time)},
              {'Lane': 4, 'No_of_Cars': lane4, 'Time' : round(lane4_time)}]

      sorted_list = sorted(list, key=itemgetter('No_of_Cars'))

      for lane in sorted_list:
        print(lane, "\n")

      
      print("Total Number of Cars is: ", total)
      print("Complete Cycle time is: ", round(total_time))

queue()

timecalc() 