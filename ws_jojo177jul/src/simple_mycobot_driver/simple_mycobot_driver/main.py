import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
import threading

from simple_mycobot_driver.gui_window import MyCobotWindow
from simple_mycobot_driver.robot_interface import RobotInterface     

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32MultiArray # For GUI to send/receive messages

class GuiRosClient:
    def __init__(self, node_name='mycobot_gui_client'):
        
        self._node = rclpy.create_node(node_name)
        self._node.get_logger().info(f'{node_name} ROS Client initialized.')

        # GUI -> Robot commands
        self.target_angles_publisher = self._node.create_publisher(
            Float32MultiArray,
            'mycobot/target_angles',
            10
        )
        
        # Robot -> GUI status/joint_states (example subscriptions)
        self.joint_state_subscription = self._node.create_subscription(
            JointState,
            'joint_states',
            self.joint_state_callback,
            10
        )
        self._node.get_logger().info('Subscribed to joint_states topic.')
        
        self.robot_status_subscription = self._node.create_subscription(
            String,
            'robot_status',
            self.robot_status_callback,
            10
        )
        self._node.get_logger().info('Subscribed to robot_status topic.')
        
        self.last_joint_states = None
        self.last_robot_status = "No status received."

        
    def publish_target_angles(self, angles_list):
        msg = Float32MultiArray()
        msg.data = [float(a) for a in angles_list]
        self.target_angles_publisher.publish(msg)
        self._node.get_logger().info(f"GUI publishing target angles: {angles_list}")

    def joint_state_callback(self, msg):
        self.last_joint_states = msg.position
        # You would update your GUI elements here based on msg.position
        # Example: self.window.update_joint_display(msg.position)
        self._node.get_logger().debug(f"Received joint states: {msg.position}")

    def robot_status_callback(self, msg):
        self.last_robot_status = msg.data
        # You would update a status bar or log in your GUI
        # Example: self.window.update_status_bar(msg.data)
        self._node.get_logger().debug(f"Received robot status: {msg.data}")

    def destroy(self):
        self._node.destroy_node()

# --- Main Application Execution ---
def main(args=None):
    rclpy.init(args=args) # Initialize ROS 2 for the GUI client
    
    # Initialize PyQt application
    app = QApplication(sys.argv)

    # Create the ROS 2 client for the GUI
    ros_client = GuiRosClient()

    # Create your GUI window and pass the ROS client to it
    window = MyCobotWindow(ros_client=ros_client) # Modify MyCobotWindow to accept this client
    window.show()

    # Spin ROS 2 in a separate thread to allow the GUI main loop to run freely
    # This is often needed when the GUI's event loop (app.exec_()) is blocking
    spin_thread = threading.Thread(target=rclpy.spin, args=(ros_client._node,))
    spin_thread.daemon = True # Allow the thread to exit when the main program exits
    spin_thread.start()

    # Start the PyQt main event loop
    ret = app.exec_()

    # Clean up after GUI exits
    ros_client.destroy() # Destroy the lightweight ROS node
    rclpy.shutdown() # Shutdown rclpy

    sys.exit(ret)



if __name__ == "__main__":
    main()
