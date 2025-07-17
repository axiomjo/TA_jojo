from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD # For Raspberry Pi version of myCobot


import time
import numpy as np
from utils import is_safe


import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Float32MultiArray # Example messages for communication
from geometry_msgs.msg import Pose # Example for sending/receiving poses
from sensor_msgs.msg import JointState # Standard for joint states


class RobotInterfaceNode(Node):
    def __init__(self):
        
        super().__init__('robot_interface_node') # Name of this ROS 2 node
        self.get_logger().info('Robot Interface Node started.')
        
        self.mc = MyCobot(PI_PORT, PI_BAUD)
        time.sleep(1)
        
        # --- ROS 2 Publishers ---
        # Example: Publish current joint states
        self.joint_state_publisher = self.create_publisher(JointState, 'joint_states', 10)
        # Example: Publish robot status or errors
        self.status_publisher = self.create_publisher(String, 'robot_status', 10)
        
        # --- ROS 2 Subscribers ---
        # Example: Subscribe to commands from the GUI (e.g., target angles)
        self.target_angles_subscriber = self.create_subscription(
            Float32MultiArray,
            'mycobot/target_angles',
            self.target_angles_callback,
            10
        )
        
        self.get_logger().info('Subscribed to mycobot/target_angles topic.')

        # --- ROS 2 Timers ---
        # Timer to periodically read and publish joint states
        self.joint_read_timer = self.create_timer(0.1, self.publish_joint_states) # Read every 100ms


     def target_angles_callback(self, msg):
        """Callback for receiving target joint angles from the GUI."""
        if self.mc:
            angles = [float(a) for a in msg.data]
            speed = 50 # Example default speed, consider making this a parameter or part of the message
            self.get_logger().info(f"Received target angles: {angles}. Moving robot.")
            try:
                self.mc.send_angles(angles, speed)
            except Exception as e:
                self.get_logger().error(f"Error sending angles to MyCobot: {e}")
                self.status_publisher.publish(String(data=f"Error: {e}"))
        else:
            self.get_logger().warn("Robot not connected. Cannot send angles.")
            self.status_publisher.publish(String(data="Error: Robot not connected."))
    
    def publish_joint_states(self):
        """Periodically reads joint states from MyCobot and publishes them."""
        if self.mc:
            try:
                angles = self.mc.get_angles()
                if angles:
                    js_msg = JointState()
                    js_msg.header.stamp = self.get_clock().now().to_msg()
                    js_msg.name = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6'] # Match your robot's joint names
                    js_msg.position = [a * 3.1415926535 / 180.0 for a in angles] # Convert degrees to radians
                    self.joint_state_publisher.publish(js_msg)
                else:
                    self.get_logger().warn("Could not get angles from MyCobot.")
            except Exception as e:
                self.get_logger().error(f"Error getting/publishing joint states: {e}")
                self.status_publisher.publish(String(data=f"Error getting joint states: {e}"))
        else:
            self.get_logger().warn("Robot not connected. Cannot publish joint states.")

    def get_joint_angles(self):
        return self.mc.get_angles()

    def get_end_effector_coords(self):
        return self.mc.get_coords()

    def incremental_move(self, direction, step=10):
        coord = self.get_end_effector_coords()
        if direction == "+X": coord[0] += step
        elif direction == "-X": coord[0] -= step
        elif direction == "+Y": coord[1] += step
        elif direction == "-Y": coord[1] -= step
        elif direction == "+Z": coord[2] += step
        elif direction == "-Z": coord[2] -= step

        if not is_safe(coord):
            return False, "⚠️ Movement unsafe or out of bounds."

        self.mc.send_coords(coord, 50, 0)
        return True, ""

def main(args=None):
    rclpy.init(args=args)
    robot_node = RobotInterfaceNode()
    rclpy.spin(robot_node)
    robot_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
     main()