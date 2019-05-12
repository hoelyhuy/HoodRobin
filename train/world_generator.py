import random
import time

def spawn_ebaniy_mob():
    random.seed(time.time())
    return ' x="' + str(random.randint(290,310)) + '" y="' + str(227) + \
        '" z="' + str(random.randint(350,368)) + '" '
def GetMissionXML(summary):
    ''' Build XML mission'''
    sheep_mob = 'type="Sheep"'
    pig_mob = 'type="Pig"'
    cow_mob = 'type="Cow"'
    polarbear_mob = 'type="PolarBear"'
    fence = 'type="fence_gate"'
    missionXML = '''<?xml version="1.0" encoding="UTF-8" ?>
                <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                <About>
                <Summary>''' + summary + '''</Summary>
              </About>
              
              <ServerSection>
                <ServerInitialConditions>
                  <Time>
                      <StartTime>1000</StartTime>
                      <AllowPassageOfTime>false</AllowPassageOfTime>
                  </Time>
                  <Weather>clear</Weather>
                </ServerInitialConditions>
                <ServerHandlers>
                  <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1"/>
                  <DrawingDecorator>
                      <DrawEntity ''' + spawn_ebaniy_mob() + sheep_mob + '''/>
                      <DrawEntity ''' + spawn_ebaniy_mob() + sheep_mob + '''/>
                      <DrawEntity ''' + spawn_ebaniy_mob() + pig_mob + '''/>
                      <DrawEntity ''' + spawn_ebaniy_mob() + pig_mob + '''/>
                      <DrawEntity ''' + spawn_ebaniy_mob() + cow_mob + '''/>
                      <DrawEntity ''' + spawn_ebaniy_mob() + cow_mob + '''/>
                      <DrawLine x1="290" y1="227" z1="349" x2="310" y2="227" z2="349" type="jungle_fence"/>
                      <DrawLine x1="289" y1="227" z1="349" x2="289" y2="227" z2="369" type="jungle_fence"/>
                      <DrawLine x1="290" y1="227" z1="369" x2="310" y2="227" z2="369" type="jungle_fence"/>
                      <DrawLine x1="311" y1="227" z1="349" x2="311" y2="227" z2="369" type="jungle_fence"/>
                  </DrawingDecorator>
                  <ServerQuitFromTimeUp timeLimitMs="300000"/>
                  <ServerQuitWhenAnyAgentFinishes/>
                </ServerHandlers>
              </ServerSection>
              
              <AgentSection mode="Survival">
                <Name>MalmoTutorialBot</Name>
                <AgentStart>
                    <Placement x="300.0" y="227.0" z="359.0" yaw="0"/>
                    <Inventory>
                        <InventoryItem slot="36" type="diamond_boots"/>
                        <InventoryItem slot="37" type="golden_leggings"/>
                        <InventoryItem slot="38" type="diamond_chestplate"/>
                        <InventoryItem slot="39" type="diamond_helmet"/>
                        <InventoryItem slot="0" type="diamond_sword"/>
                    </Inventory>
                </AgentStart>
                <AgentHandlers>
                  <ObservationFromFullStats/>
                  <ContinuousMovementCommands turnSpeedDegs="180"/>
                  <VideoProducer
                    want_depth="0"
                    viewpoint="0">
                        <Width> 800 </Width>
                        <Height> 500 </Height>
                  </VideoProducer>
                </AgentHandlers>
              </AgentSection>
            </Mission>'''

    return missionXML

