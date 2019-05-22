'''
AI that can recognize enemies and kill enemies
'''
from __future__ import division
import numpy as np

import MalmoPython
import os
import random
import sys
import time
import json
import math
import errno
from collections import defaultdict, deque
from timeit import default_timer as timer


import world_generator
import imageprocessing
from darkflow.net.build import TFNet
import cv2
import parse_detection


if __name__ == '__main__':
    random.seed(0)
    c = 1
    print('Starting...', flush=True)
    agent_host = MalmoPython.AgentHost()
    try:
        agent_host.parse( sys.argv )
    except RuntimeError as e:
        print('ERROR:',e)
        print(agent_host.getUsage())
        exit(1)
    if agent_host.receivedArgument("help"):
        print(agent_host.getUsage())
        exit(0)
    num_reps = 1
    options = {"model": "cfg/yolo_custom.cfg", "load": -1, "threshold": 0.1}
    tfnet = TFNet(options)
    for iRepeat in range(num_reps):
        my_mission = MalmoPython.MissionSpec(world_generator.GetMissionXML("Go Kill #" + str(iRepeat)), True)
        my_mission_record = MalmoPython.MissionRecordSpec()
        #my_mission.requestVideo(800, 500)
        #my_mission.setViewpoint(0)
        
        # Attempt to start a mission:
        max_retries = 3
        for retry in range(max_retries):
            try:
                agent_host.startMission( my_mission, my_mission_record )
                break
            except RuntimeError as e:
                if retry == max_retries - 1:
                    print("Error starting mission:",e)
                    exit(1)
                else:
                    time.sleep(2)        
    # Loop until mission starts:
    print("Waiting for the mission to start ", end=' ')
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        print(".", end="")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print("Error:",error.text)
    print()
    print("Mission running ", end=' ')
    past_time = time.time()
    
    # Loop until mission ends:
    while world_state.is_mission_running:
        print(".", end="")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        for error in world_state.errors:
            print("Error:",error.text)
        if world_state.number_of_video_frames_since_last_state > 0:
                cur_time = time.time()
                if cur_time - past_time > 5:
                    print("image to save!")
                    img = world_state.video_frames[-1].pixels
                    imageprocessing.saveArrayAsImg(img, 800, 500, "./capture/" + "current_capture"  + ".jpg",
                                   "./screenshots/" + "_"  + str(c) + "_d" + ".jpg")
                    print("screenshot saved")
                    imgcv = cv2.imread("./capture/current_capture.jpg")
                    result = tfnet.return_predict(imgcv)
                    print(result)
                    x, y = parse_detection.target_position(result, "pig")
                    print("The pig is at, ", x, y, " on the screen")
                    if x > 0.0 and y > 0.0:
                        parse_detection.aim(x, y, agent_host)
                        parse_detection.attack(agent_host)   
                    c += 1
                    past_time = cur_time

    print()
    print("Mission ended")
    # Mission has ended.
