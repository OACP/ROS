import rospy
from std_msgs.msg import String
from hello_world.msg import Position

def talker():

    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chatter', Position, queue_size=10)
    rate = rospy.Rate(1) # 10hz

    while not rospy.is_shutdown():
        #msg = "hello world %s" % rospy.get_time()
        msg = Position()
        msg.message = "My position is: "
        msg.x = 2.0
        msg.y = 1.5
        #rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass