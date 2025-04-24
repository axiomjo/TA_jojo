"""
Explanation of (central_point_estimator.py) object_position_estimator.py:

It creates a ROS 2 node named object_position_estimator.
It subscribes to the /webcam/image_raw topic to receive image frames.
It publishes the estimated object position on the /object_position topic using a custom message type ObjectPosition.
The image_callback function receives the image, performs (simulated) object detection and pose estimation, and publishes the result. You will need to replace the simulation part with your actual image processing and 3D pose estimation logic.
"""




import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from your_package_name.msg import ObjectPosition  # Create this custom message
from cv_bridge import CvBridge
import cv2
import numpy as np
import random  # For simulating object position

class ObjectPositionEstimator(Node):
    def __init__(self):
        super().__init__('object_position_estimator')
        self.subscription = self.create_subscription(
            Image,
            '/webcam/image_raw',
            self.image_callback,
            10
        )
        self.publisher_ = self.create_publisher(ObjectPosition, '/object_position', 10)
        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            # Simulate object detection (replace with your actual logic)
            object_detected = random.random() > 0.5
            if object_detected:
                # Simulate 3D position (replace with your actual pose estimation)
                x = random.uniform(0.1, 1.0)
                y = random.uniform(-0.5, 0.5)
                z = random.uniform(0.5, 1.5)

                position_msg = ObjectPosition()
                position_msg.x = x
                position_msg.y = y
                position_msg.z = z
                self.publisher_.publish(position_msg)
                self.get_logger().info(f'Detected object at: x={x:.2f}, y={y:.2f}, z={z:.2f}')
            else:
                self.get_logger().info('No object detected in this frame')

        except Exception as e:
            self.get_logger().error(f'Error processing image: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = ObjectPositionEstimator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt, shutting down.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
