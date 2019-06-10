---
layout: default
title: Final Report
---
## Video
## Project Summary
In our Minecraft-AI project, the agent tries to recognize different animals that appear in his view such as Pig, Rabbit, Ozelot, Sheep, Cow and then attempts to attack the Pig with a bow and arraows. Since we are interested in computer vision, we will attempt to use a real-time object detection algorithm called YOLO (You Only Look Once) to detect to detect which animals are in the agents view and where are the animals in the agent's view. Object detection can be very slow if we don't have the right approach. For instance, given an image and the objective to detect the objects in the image, one naive solution is to predict all the possible bounding box that we can draw in the image, which is very inefficient. Inorder to detect objects in real-time, we need a more sophisticated algorithm that run fast but still gives correct predictions with high accuracy.
## Approaches
Firstly, we write a program to generate the dataset, which is a set of many image captures of the agent's view. To do this, we start with designing the world, which is a piece of farmland surrounded by fences on four sides. On that piece of land, we spawn some animals (such as pigs, cows, sheeps, etc) at random locations. As the program starts, the agents takes a screenshot of his current view every 3 seconds. Malmo can give us the latest frame in the form of array of pixels. Given the array of pixels, we use image processing tools such as Pillow and opencv to convert the array of pixels into an image file and store it to our computer. Before, we trained our neural network on a dataset of about 400 screenshots and the agent performs quite well. For final submission, we decided to train our neural network on about 1300 images to improve the accuracy of object detection.
<br /> <br />
After collecting the screenshots, we use an image labeling tool, which is called labelImg to create annotation files for the screenshots. An annotation file is an additional file that tells more information about the image; for this project, the additional information is which objects are in the image and where are they in the image. labelImg allows us to draw bounding box around an object and label that object, then generate an annotation file that is need for training. 
<br /> <br />
We will be using a real-time object detection algorithm called YOLO (You Only Look Once) to detect the animals in the agent's view. How the object detection algorithm works is that we apply a single neural network to the full image. This network divdes the image into regions and predict bounding boxes and probabilities for each region. These bounding boxes are weighted by the predicted probabilities. The model has several advantages over classifier-based systems. It looks at the whole image at test time so its predictions are informed by global context in the image. It also makes predictions with a single network evaluation unlike systems like R-CNN which require thousands for a single image. This makes it extremely fast, more that 1000 times faster than R-CNN and 100 times faster than Fast R-CNN. [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/)
<br /> <br />
Darknet is an open source neural network framework written in C and CUDA. It supports both CPU and GPU computation. To carry out training and object detection, we use darkflow, which is a translation of darknet to tensorflow. Once we are done with generating the screenshots and the annotation file, we store the screenshots and the annotation files in darkflow workspace. In addition to our own dataset, we also need YOLOv2 configuration file (with some small adjustments) and YOLOv2 weights to train. For training we use Google Colab, which supports Python notebook and many other useful machine learning tools such as opencv, tensorflow, numpy, plus a free GPU that helps to improve training speed. After a number of interations of training, we look for a point where the loss converges and stop our training there.
<br /> <br />
Once we are done with training, we can use our network to detect the objects in Minecraft while the game is running. Darkflow returns image detection results in a form of json array of json object. Each json object contains the information about the label of the object, its bounding box which is specified by the coordinate of the top left corner and the coordinate of the bottom right corner, confidence level of prediction. We extract this information to find the center of the bounding box around the target object (midpoint of the 2 corner points) that we are most confident about and then move the agent's aim towards that point and then shoot an arrow at the target.
## Evaluation
#### How does YOLO make decisions about object detection
YOLO divides the input image into an SxS grid. For each grid cell, it predicts B boundary boxes, which are defined by the algorithm, and each box has one box confidence score. Each grid cell predicts only one object.
some image here
Each boundary box contains 5 elements: (x,y,w,h) and a box confidence score. The confidence score reflects how likely the box contains an object (objectness) and how accurate is the boundary box. Given that there are SxS grid cells and each grid cell predicts B boundary box, we can compute SxSxB box confidence scores. However, we only keep the boundary boxes with high box confidence score (greater than 0.25) and discard the boxes with low confidence score. The conditional class probability is the probability that the detected object belongs to a particular class (one probability per category for each cell). The class confidence score for each prediction box is computed as:
<br /> <br />
class confidence score = box confidence score * conditional class probability
<br /> <br />
The class confidence score measures the confidence on both the classification and the localization, which is where an object is located. 
<br /> <br /> box confidence score = P(object) * IoU
<br /> conditional class probability = P(class i | object)
<br /> class confidence score = P(class i) * IoU <br /> 
* Where:
	* P(object) is the probability the box contains an object.
	* IoU is the intersection over union between the predicted box and the ground truth.
	* P(class i | object) is the probability the object belongs to class i given an object is presence.
	* P(class i) is the probability the object belongs to class i.
<br /> <br />

Before incorporating our network into the game we need to evaluate its performance. For setting up the evaluation, we generate 300 test image, run darkflow on the test data once with the model from previous submission and once with model that we just trained on a bigger size dataset (about 900 images) and compare the performances of the two models.

<br /> The metric that we use to measure performance is accuracy which is the number of correct detections over the total number of objects. The correct detections and the objects are counted manually. The overall accuracy is computed by taking the ratio of correct detections (can be from any class) to total objects. In addition to the overall accuracy, we also compute 5 class accuracies for the 5 object types (pig, cow, sheep, ozelot, rabbit), because we are interested in whether there is an improvement on each of the object type. Class accuracy is computed by taking the ratio of correct detection of that class over total objects of that class; for example, the number of correctly detected pigs over total pigs.
<br />
<br />
## References
[Image Processing](https://github.com/jennyzeng/Minecraft-AI)
<br />
[Image Labeling software](https://github.com/tzutalin/labelImg)
<br />
[YOLO: Real-Time Object Detection (Tensorflow)](https://github.com/thtrieu/darkflow)
<br />
[YOLO: Real-Time Object Detection (C)](https://pjreddie.com/darknet/yolo/)
<br />
[Project inspiration](https://www.youtube.com/watch?v=4eIBisqx9_g&t=444s)
