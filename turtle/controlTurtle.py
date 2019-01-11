#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def move():
    vel_msg = Twist()
    vel_msg.linear.x = 1
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    return vel_msg


def move_distance(rate, pub, distance):
    currentDistanceX = 0
    while (currentDistanceX < distance):
        vel_msg = move()
        pub.publish(vel_msg)
        currentDistanceX = currentDistanceX + 1
        rate.sleep()


def talker():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('controlTurtle', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    move_distance(rate, pub, 30)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
