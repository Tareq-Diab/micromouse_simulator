#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from dualwheelbot.msg import data
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist
import numpy as np
import math
import time
import matplotlib.pyplot as plt
x=0
y=0
z=0
roll=0
pitch=0
yaw=0
error_log=[]
def extractor(odom):
    global x,y,z,roll,pitch,yaw
    #print(odom.pose)
    pose=odom.pose.pose.position
    x=pose.x
    y=pose.y
    z=pose.z
    ori=odom.pose.pose.orientation
    ori_list=[ori.x,ori.y,ori.z,ori.w]
    roll,pitch,yaw=euler_from_quaternion(ori_list)



rospy.init_node("localizer")
sub=rospy.Subscriber("/odom",Odometry,callback=extractor)
pub=rospy.Publisher("/cmd_vel",Twist,queue_size=10)
twist=Twist()

r=rospy.Rate(10)
def conv(a):
    return (a+6.24)%6.24

def goto(x_g,y_g):
    global x,y,z,roll,pitch,yaw,error_log
    local_error=[]
    local_error_time=[]

    while not rospy.is_shutdown():
        
        rospy.wait_for_message("/odom",Odometry)
        #linear speed 
        distance=np.sqrt((x_g-x)**2+((y_g-y)**2))
        kp=0.1
        speed=kp*distance
        twist.linear.x=speed

        angel=math.atan2(y_g-y,x_g-x)
        yaw=yaw
        kpa=1
        error=angel-yaw
        if ((angel > 1.57) or (angel < -1.57)) and ((error > 3.14) or (error < -3.14)):
            print("special condition")
            if error >  3.14 :
                error=abs(error)-6.28
            if error < -3.14 :
                error=6.28-abs(error)


        angularspeed=kpa*(error)
        twist.angular.z=angularspeed


        pub.publish(twist)

        local_error.append(distance)
        local_error_time.append(int(time.time()))


        
        if distance<0.03:
            twist.linear.x=0
            twist.angular.z=0
            pub.publish(twist)
            error_log.append([local_error,local_error_time])
            print("reached error={}".format(distance))
            break
def rotat(x_g,y_g):
    while not rospy.is_shutdown():
        global x,y,z,roll,pitch,yaw
        rospy.wait_for_message("/odom",Odometry)


        angel=math.atan2(y_g-y,x_g-x)
        yaw=yaw
        kpa=2

        error=angel-yaw
        if ((angel > 1.57) or (angel < -1.57)) and ((error > 3.14) or (error < -3.14)):
            print("special condition")
            if error >  3.14 :
                error=abs(error)-6.28
            if error < -3.14 :
                error=6.28-abs(error)


        angularspeed=kpa*(error)
        twist.angular.z=angularspeed
        
        
        print("angel={}, yaw={} ,error={}".format(angel,yaw,error))


        pub.publish(twist)
        

        
        if (abs(angel-yaw))<0.05:
            twist.linear.x=0
            twist.angular.z=0
            #pub.publish(twist)

            print("rotated to{},{}".format(x_g,y_g))
            break
def move (x,y):
    xm=(0.18*x)+0.099
    ym=-((0.18*y)+0.099)
    print(xm,ym)
    rotat(xm,ym)
    time.sleep(0.5)
    goto(xm,ym)

           
           
if __name__ == "__main__":

    move(5,0)
    move(5,1)
    move(1,1)
    move(1,4)
    move(2,4)
    move(2,2)
    move(7,2)
    move(7,1)
    move(8,1)
    move(8,0)
    move(13,0)
    move(13,2)
    move(12,2)
    move(12,3)
    move(10,3)
    move(10,4)
    move(3,4)
    move(3,5)
    move(4,5)
    move(4,6)
    move(5,6)
    move(5,5)
    move(11,5)
    move(11,6)
    move(10,6)
    move(10,7)
    move(7,7)
    