#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import NavSatFix

g_received = False
g_gps_fixed = NavSatFix()

def gps_callback(data):
    global g_received
    global g_gps_fixed
    g_gps_fixed = data
    g_gps_fixed.header.frame_id = "summit_xl_gps_base_link"
    g_received = True    
    
    
def fix_gps_data():
    global g_received
    global g_gps_fixed
    rospy.init_node("fix_gps_data")

    rospy.Subscriber('summit_xl/fix', NavSatFix, gps_callback)

    gps_pub = rospy.Publisher('gps_fixed', NavSatFix, queue_size=5)

    rate = rospy.Rate(10) # 10Hz
    while (not rospy.is_shutdown()):
        if g_received:
            gps_pub.publish(g_gps_fixed)
        rate.sleep()


if __name__ == '__main__':
    fix_gps_data()
