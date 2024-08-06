# Final-Year-Project
Source Code for my Final Year Project which is Titled as Density Based Traffic Control System..

The system is designed in python and it uses image processing via yolov3 to identify and count the number of cars in images.
Yolov3 was trained on the MSCOCO Dataset.

The system first detects cars in an image and counts them. After which,the time to be alloted to a particular lane is calculated based on the number of cars present.

**Mini Instrictions**

1. Download and Install Python

2. Make sure its installed by typing "python --version" in CMD.. This should output the Python version

3. Install opencv pytion by typing "pip install opencv-python" in terminal.. It should also download Numpy

4. Instal PyQt5 by typing "pip install PyQt5" in terminal

5. Add yolov3.cfg and yolo.weights in your file directory.. can be downloaded from "https://pjreddie.com/media/files/yolov3.weights"

6. Add 4 images with cars and check add their exact names/paths in function ProcessImg() on line 78 in DBTCS.py

7. Execute UI.py and Enjoy!!!!!
 
Credits to [insert crisis here] as well as WeziMk for their help during the development of this project..
For any queries dont hesitate to contact me via email @ mazubapp@gmail.com :)
