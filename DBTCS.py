import cv2
import numpy as np
from operator import itemgetter


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
    CarCount = 0
    TruckCount = 0
    MotorbikeCount = 0
    CarTotal = 0

    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 0.5, color, 0)
            
            #Vehicle Count
            CarCount += label.count('car')
            TruckCount += label.count('truck')
            MotorbikeCount += label.count('motorbike')

            CarTotal = CarCount + TruckCount + MotorbikeCount

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return CarTotal

# lane1 = 0
# lane2 = 0
# lane3 = 0
# lane4 = 0
# total = 0
def ProcessImg():
    #Process Traffic from 4 Lanes
    lane1 = ImgProcess("traff5.jpg")
    lane2 = ImgProcess("traff4.jpg")
    lane3 = ImgProcess("traff6.jpg")
    lane4 = ImgProcess("em.jpeg")
    # total = lane1 + lane2 + lane3 + lane4

    return [lane1, lane2, lane3, lane4]
#ProcessImg()


# lane1_time = 0
# lane2_time = 0
# lane3_time = 0
# lane4_time = 0
# total_time = 0


def time(lanes, delay):
    # global total_time, lane1_time, lane2_time, lane3_time, lane4_time
    
    total = sum(lanes)

    lane1_time = (lanes[0]/total) * delay
    lane2_time = (lanes[1]/total) * delay
    lane3_time = (lanes[2]/total) * delay
    lane4_time = (lanes[3]/total) * delay

    return [round(lane1_time), round(lane2_time), round(lane3_time), round(lane4_time)]

def queue(lanes, times, variance):

    total_time = sum(times)
    total = sum(lanes)

    list = [{'Lane': 1, 'TotalVehicles': lanes[0], 'Time' : round(times[0])},
              {'Lane': 2, 'TotalVehicles': lanes[1], 'Time' : round(times[1])},
              {'Lane': 3, 'TotalVehicles': lanes[2], 'Time' : round(times[2])},
              {'Lane': 4, 'TotalVehicles': lanes[3], 'Time' : round(times[3])}]


    sorted_list = sorted(list, key=itemgetter('TotalVehicles'), reverse=variance)

    for lane in sorted_list:
        print(lane, "\n")

      
    print("Total Number of Vehicles is: ", total)
    print("Complete Cycle time is: ", round(total_time))

    return sorted_list

def execute(delay, variance):
    lanes = ProcessImg()
    times = time(lanes, delay)
    return queue(lanes, times, variance)
