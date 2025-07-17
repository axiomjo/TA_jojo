from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='simple_mycobot_driver',
            executable='robot_interface_node', # Name of the executable for the robot interface
            name='node_mycobot_interfacekerobot',             # ROS node name
            output='screen',
            parameters=[
                # Add parameters for your robot interface, e.g., serial port, baud rate
                {'port': '/dev/ttyAMA0'},
                {'baudrate': 1000000}
            ]
        ),
        
        Node(
            package='simple_mycobot_driver',
            executable='mycobot_gui_node', # Name of the executable for the GUI
            name='node_lappy_GUInya',            # ROS node name for the GUI application
            output='screen',
            # Add parameters for your GUI, if any
        )
    ])
