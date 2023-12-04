#!/usr/bin/python3
import rospy
from actions_tutorial.msg import WashTheDishesAction,WashTheDishesResult,WashTheDishesFeedback
import actionlib
import math
from turtlesim.srv import TeleportRelativeRequest,TeleportRelativeResponse
i=5.544445
j=5.544445
last_postion_x=0
last_postion_y=0
class Response(): 
    def __init__(self):
        rospy.init_node("Response")
        self.x=None
        self.y=None
        self.limit=None
        self.postion_2=WashTheDishesAction()
        self.feedback=WashTheDishesFeedback()
        self.distance=WashTheDishesResult()
        self.main_srv=actionlib.SimpleActionServer("server_turtule",WashTheDishesAction,self.callback)
        self.turtlesrv=rospy.ServiceProxy("teleport_relative",TeleportRelativeRequest)
       

    def callback(self,postion):
        for i in range(self.postion_2.x):
            for j in range(self.postion_2.y):
                self.x=math.pow((i-last_postion_x),2)
                self.y=math.pow((j-last_postion_y),2)
                self.distanceNow=math.sqrt(self.x+self.y)
                last_postion_x=i
                last_postion_y=j
                self.main_srv.publish_feedback(self.distance)
                WashTheDishesResult.distance=self.distance
                self.turtle_move(WashTheDishesResult.distance)
                break
    

    def turtle_move(self,reqst_2):
        TeleportRelativeRequest.linear=reqst_2
        return TeleportRelativeResponse

if __name__=='__main__':
  try:
    server_std=Response()
    rospy.spin()
  except rospy.ROSInterruptException():
     pass

        

