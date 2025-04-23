import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image  # Assuming /raw_cam publishes sensor_msgs/Image
from cv_bridge import CvBridge  # To convert ROS Image to OpenCV format
import cv2  # OpenCV for image manipulation (optional, for display)
from PyQt5.QtGui import QImage, QPixmap  # For displaying images in Qt

class Ros2Thread(QThread):
    image_received = pyqtSignal(QImage)

    def __init__(self):
        QThread.__init__(self)
        rclpy.init()
        self.node = Node('qt_camera_subscriber')
        self.subscription = self.node.create_subscription(
            Image,
            '/image_raw',
            self.listener_callback,
            10
        )
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            h, w, ch = cv_image.shape
            bytes_per_line = ch * w
            q_image = QImage(cv_image.data, w, h, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            self.image_received.emit(q_image)
        except Exception as e:
            print(f"Error converting image: {e}")

    def run(self):
        rclpy.spin(self.node)
        rclpy.shutdown()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ros_thread = Ros2Thread()
        self.initUI()
        self.ros_thread.image_received.connect(self.update_image)
        self.ros_thread.start()

    def initUI(self):
        self.setWindowTitle("ROS 2 Camera Viewer")
        self.setGeometry(100, 100, 640, 480)  # Adjust size as needed

        self.image_label = QLabel(self)
        self.image_label.resize(640, 480)  # Initial size

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

    @pyqtSlot(QImage)
    def update_image(self, img):
        pixmap = QPixmap.fromImage(img)
        self.image_label.setPixmap(pixmap)

    def closeEvent(self, event):
        self.ros_thread.quit()
        self.ros_thread.wait()
        event.accept()

def main(args=None):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
