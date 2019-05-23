---
layout: default
title:  Home
---

[Source code](https://github.com/hoelyhuy/HoodRobin)

## Reports:

- [Proposal](proposal.html)
- [Status](status.html)
- [Final](final.html)

![Alt Text](https://media.giphy.com/media/qYV4rEOtu7k4M/giphy.gif)

## What is our project about?
For our project, we will use computer vision to detect objects that are currently in the view of the agent and try to atack the target object. We choose the target object to be Pigs, and our agent will try to shoot an arrow at pigs. Using an Object Detection algorithm called YOLO (You Only Look Once), we are able to detect the objects in the agents 2D view which might be Sheeps, Pigs, Cows, Rabbits, Ozelots. From that, we can detect where our target is, move our aim towards target and shoot an arrow at the target. 
Our dataset is generated from Malmo Minecraft as image files and we use an image labeling software to label those images. We will use our data (about 1300 images by time of final submission) to train our neural network for object detection. 
<br />
# Input
![alt text](input_index.jpg)
# Output
![alt text](output_index.jpg)
<br />
## Team members
Edwin Li
<br />
Ban Gia Tien
<br />
Huy Minh Brian Pham

## Resources used
[Image Capture](https://github.com/jennyzeng/Minecraft-AI)
<br />
[Image Labeling software](https://github.com/tzutalin/labelImg)
<br />
[YOLO Object Detection (You Only Look Once)](https://github.com/thtrieu/darkflow)

