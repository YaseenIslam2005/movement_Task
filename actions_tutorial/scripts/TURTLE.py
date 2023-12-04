#!/usr/bin/python3
import rospy
import actionlib
from actions_tutorial.action import WashTheDishesAction
import sys

class Caller():
    def __init__(self):
           rospy.init_node("caller")
           self.rqst=rospy.ServiceProxy("server_turtule",WashTheDishesAction)
           



    def readCoordinates(self):
        WashTheDishesAction.x=sys.argv(int[1])
        WashTheDishesAction.y=sys.argv(int[2])
    
if __name__=='__main__':
     try:
      caller_1=Caller()
      caller_1.readCoordinate()
     except rospy.ROSInterruptException:
         pass

