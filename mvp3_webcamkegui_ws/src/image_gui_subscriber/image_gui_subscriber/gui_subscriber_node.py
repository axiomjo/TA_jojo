import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QTextEdit, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer

class ImageSubscriberNode(Node):
    def __init__(self, update_callback):
        super().__init__('image_gui_subscriber')
        self.subscriber = self.create_subscription(Image, 'webcam/image_raw', self.listener_callback, 10)
        self.bridge = CvBridge()
        self.latest_frame = None
        self.update_callback = update_callback

    def listener_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        self.latest_frame = cv_image
        self.update_callback(cv_image)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Webcam Viewer")
        self.image_label = QLabel()
        self.instruction_text = QTextEdit("Welcome!\\n\\nThis GUI subscribes to webcam image topic and displays it here.\\nMake sure to run the publisher node separately.")
        self.instruction_text.setReadOnly(True)

        layout = QHBoxLayout()
        layout.addWidget(self.instruction_text)
        layout.addWidget(self.image_label)

        self.setLayout(layout)

        rclpy.init()
        self.node = ImageSubscriberNode(self.update_image)
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: rclpy.spin_once(self.node, timeout_sec=0))
        self.timer.start(30)

    def update_image(self, frame):
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        self.image_label.setPixmap(pixmap)

    def closeEvent(self, event):
        self.node.destroy_node()
        rclpy.shutdown()
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
