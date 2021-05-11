import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import threading
from IPython import get_ipython
from operator import itemgetter

def lane_1():
    #read image from local folder/directory
    im = cv2.imread("/content/drive/My Drive/Colab_Data/traff.jpg")

    plt.imshow(im)
    plt.show(None)

    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    plt.imshow(output_image)
    plt.show()
    print('Number of cars in lane 1 is ' + str(label.count('car')))

    global num1

    num1 = int(str(label.count('car')))
  
def lane_2():
    #read image from local folder/directory
    im = cv2.imread("/content/drive/My Drive/Colab_Data/traff5.jpg")


    plt.imshow(im)
    plt.show(None)

    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    plt.imshow(output_image)
    plt.show()
    print('Number of cars in lane 2 is ' + str(label.count('car')))

    global num2

    num2 = int(str(label.count('car')))

def lane_3():
    #read image from local folder/directory
    im = cv2.imread("/content/drive/My Drive/Colab_Data/traff6.jpg")

    plt.imshow(im)
    plt.show(None)

    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    plt.imshow(output_image)
    plt.show()
    print('Number of cars in lane 3 is ' + str(label.count('car')))

    global num3

    num3 = int(str(label.count('car')))

def lane_4():
    #read image from local folder/directory
    im = cv2.imread("/content/drive/My Drive/Colab_Data/traff7.jpg")

    plt.imshow(im)
    plt.show(None)

    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    plt.imshow(output_image)
    plt.show()
    print('Number of cars in lane 4 is ' + str(label.count('car')))

    global num4
    
    num4 = int(str(label.count('car')))

lane_1()
lane_2()
lane_3()
lane_4()




def time():
      global total, total_time, lane1_time, lane2_time, lane3_time, lane4_time 

      total = num1 + num2 + num3 + num4
      
      lane1_time = (num1/total) * 60
      lane2_time = (num2/total) * 60
      lane3_time = (num3/total) * 60
      lane4_time = (num4/total) * 60

      total_time = lane1_time + lane2_time + lane3_time + lane4_time

time()

def queue():

      list = [{'Lane': 1, 'No_of_Cars': num1, 'Time' : round(lane1_time)},
              {'Lane': 2, 'No_of_Cars': num2, 'Time' : round(lane2_time)},
              {'Lane': 3, 'No_of_Cars': num3, 'Time' : round(lane3_time)},
              {'Lane': 4, 'No_of_Cars': num4, 'Time' : round(lane4_time)}]

      sorted_list = sorted(list, key=itemgetter('No_of_Cars'))

      for lane in sorted_list:
        print(lane, "\n")

      
      print("Total Number of Cars is: ", total)
      print("Complete Cycle time is: ", total_time)

queue()

#delete variables from memory
del total, total_time, lane1_time, lane2_time, lane3_time, lane4_time
