#!/usr/bin/env python
#license removed for brevity
import rospy
from std_msgs.msg import Int16

def talker():
    pub=rospy.Publisher('chatter',Int16, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate=rospy.Rate(10)#10hz
    counter=0
    while not rospy.is_shutdown():
        num=int(input("Dame un numero entero:"))
        rospy.loginfo(num)
        pub.publish(num)
        
if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass