import MalmoPython
import time

def target_position(arr, target):
    '''return the center point of the detection box of the target animal.
    In case there are many tagets, choose the one with highest confidence
    level'''
    max_confidence = 0.0
    for detection in arr:
        if detection['label'] == target and detection['confidence'] >=  max_confidence:
            x_top = detection['topleft']['x']
            y_top = detection['topleft']['y']
            x_bot = detection['bottomright']['x']
            y_bot = detection['bottomright']['y']
            max_confidence = detection['confidence']
    if max_confidence > 0.0:
        return (x_top + x_bot) / 2.0, (y_top + y_bot) / 2.0
    else:
        return -1.0, -1.0

def aim(x, y, agent_host):
    side_change = 400.0 - x
    vertical_change = 250 - y
    if side_change > 0.0: #on the left
        turn = -1
        turn_time = (5.0 / 18.0) * (side_change / 400.0)
    elif side_change < 0.0: #on the right
        turn = 1
        turn_time = (5.0 / 18.0) * (-side_change / 400.0)
    else:
        return
    agent_host.sendCommand("turn " + str(turn))
    time.sleep(turn_time)
    agent_host.sendCommand("turn 0.0")

    if vertical_change > 0: #above
        pitch = -1
        pitch_time = (5.0 / 18.0) * (vertical_change / 400.0)
    elif vertical_change < 0: #below
        pitch = 1
        pitch_time = (5.0 / 18.0) * (-vertical_change / 400.0)
    else:
        return
    agent_host.sendCommand("pitch " + str(pitch))
    time.sleep(pitch_time)
    agent_host.sendCommand("pitch 0")
    return

def attack(agent_host):
    agent_host.sendCommand("use 1")
    time.sleep(2)
    agent_host.sendCommand("use 0") 
    return 
    
        
    
