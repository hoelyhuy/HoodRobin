---
layout: default
title: Status
---
## Project Summary
Our Minecraft-AI project will focus on recognizing different characters in Minecraft such as Pig, Rabbit, Ozelot, Sheep, Cow and then try to attack the Pig. We will be using image detection to determine what animals are in the agent's view and where are they in the view. Based on the rule that we make, which is to attack Pigs, our agent will try to aim at a pig and shoot arrows at it. 
## Approach
Firstly, we write a program to generate our dataset. This program captures the agent's view every 3 seconds and store the captures 
## Evaluation
Since our project mainly focus on image detection, the performance of the project is measured by how accurately our object detector detects the animals. After we finish training our dataset, we will test our model on a set of 100 images that are generated from the game. The accuracy is the number of correct detections over the total number of objects. These numbers are counted manually.
<br />
# Input
![alt text](https://github.com/hoelyhuy/HoodRobin/blob/master/docs/input_status.jpg)
# Output
![alt text](https://github.com/hoelyhuy/HoodRobin/blob/master/docs/output_status.jpg)
<br />
From the example above, we can see that there are a total of 6 objects in the image: a cow, an ozelot, a rabbit, and 3 pigs. Our object detector is able to correctly detect 4 objects.
## Remaining Goals and Challenges
For the remaining 2-3 weeks, we will try to improve the accuracy of our detector by training our neural network on a larger size dataset. At present, our network is trained on 400 images and has decent performance. We shoot for over 1000 images in our training dataset.
<br />
Another thing that we need to do is improving the algorithm to aim at a target object. Right now our agent can aim at the target quite well sometimes, but sometimes the agent's aiming is a bit off. 
<br />
Some limitations that we can think of are the overhead to load the agent's current view image into our neural network and the time to process the image. The total time to load and process an image is about a couple seconds. This is a bit slow for a real time application like our project, since our target might have walked away once we finish processing the previous frame. If we had a GPU we would be able to process image a lot faster and we might be able to solve the problem.
## Resources Used
[Image Capture](https://github.com/jennyzeng/Minecraft-AI)
<br />
[Image Labeling software](https://github.com/tzutalin/labelImg)
<br />
[YOLO Object Detection (You Only Look Once)](https://github.com/thtrieu/darkflow)


