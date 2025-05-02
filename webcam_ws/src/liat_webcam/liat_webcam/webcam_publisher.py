"""
Explanation of webcam_publisher.py:

It creates a ROS 2 node named webcam_publisher.
It initializes a publisher for the /webcam/image_raw topic with the sensor_msgs/msg/Image message type.
It opens the webcam using OpenCV (cv2.VideoCapture(0)).
It uses CvBridge to convert OpenCV frames to ROS 2 Image messages.
A timer is set to publish frames at approximately 30 Hz.
The publish_frame function reads a frame from the webcam and publishes it as a ROS 2 message.
The on_shutdown function releases the webcam when the node is stopped.

"""



import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class WebcamPublisher(Node):
    def __init__(self):
        super().__init__('webcam_publisher')
        self.publisher_ = self.create_publisher(Image, '/webcam/image_raw', 10)
        self.cap = cv2.VideoCapture(0)  # Use 0 for default webcam, adjust if needed
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")
        self.bridge = CvBridge()
        self.timer = self.create_timer(0.033, self.publish_frame)  # Publish at ~30 Hz

    def publish_frame(self):
        ret, frame = self.cap.read()
        if ret:
            msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.publisher_.publish(msg)
        else:
            self.get_logger().warn('No image data received from webcam')

    def on_shutdown(self):
        self.cap.release()
        self.get_logger().info('Webcam publisher shutting down.')

def main(args=None):
    rclpy.init(args=args)
    node = WebcamPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt, shutting down.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
