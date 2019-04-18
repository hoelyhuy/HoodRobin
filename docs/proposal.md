---
layout: default
title: Proposal
---
## Summary of the Project
Our Minecraft-AI project will focus on recognizing different characters in Minecraft such as creeper, skeleton, cat, pig, etc, and performing actions on those characters which depend on the rule that we make (for example kill anything but cats). The input will be agent's view at current time, and a set of rules. Our model will predict which character is in the agent's view and perform an action according to the rule set that we give beforehand.
## AI/ML Algorithms
We are planning to combine computer vision with machine learning to determine which character is in the agent's view and use reinforment learning to take action (aim and shoot if the character is in enemy list, or do nothing if character is not in enemy list).
## Evaluation Plan
The metrics are the number of correct predictions, the number of correct characters that we kill and the number of incorrect characters that we kill. The baseline metric would be attacking the incorrect character. We will try to improve the performance of our agent by maximizing the number of correct kills and minimizing the number of incorrect kill.  

We will be able to qualitatively determine whether or not our agent behaves appropriately by observing the agent's actions on the characters. As far as we plan, the agent will stare right at the character when the mission starts. All it has to do is determine the character and perform action on that character. Our moonshoot case is that the agent sees the character from far away, walk towards the character then perform an action. In order to solve this case, we might need to use computer vision to figure out the distance and direction from the agent to the character, also adjust the agents aiming so that it can accurately shoot the character.
## Appointment with the Instructor
edit text here
