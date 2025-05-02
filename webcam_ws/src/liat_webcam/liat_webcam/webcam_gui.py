import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot

import rclpy
from rclpy.node import Node
from your_package_name.msg import ObjectPosition  # Import your custom message

class PositionSubscriber(QThread):
    position_received = pyqtSignal(float, float, float)

    def __init__(self):
        QThread.__init__(self)
        rclpy.init()
        self.node = Node('qt_position_subscriber')
        self.subscription = self.node.create_subscription(
            ObjectPosition,
            '/object_position',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.position_received.emit(msg.x, msg.y, msg.z)

    def run(self):
        rclpy.spin(self.node)
        rclpy.shutdown()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.position_thread = PositionSubscriber()
        self.initUI()
        self.position_thread.position_received.connect(self.update_position)
        self.position_thread.start()

    def initUI(self):
        self.setWindowTitle("Object Position Viewer")
        self.setGeometry(100, 100, 300, 150)

        self.x_label = QLabel("X: ")
        self.y_label = QLabel("Y: ")
        self.z_label = QLabel("Z: ")

        layout = QVBoxLayout()
        layout.addWidget(self.x_label)
        layout.addWidget(self.y_label)
        layout.addWidget(self.z_label)
        self.setLayout(layout)

    @pyqtSlot(float, float, float)
    def update_position(self, x, y, z):
        self.x_label.setText(f"X: {x:.2f}")
        self.y_label.setText(f"Y: {y:.2f}")
        self.z_label.setText(f"Z: {z:.2f}")

    def closeEvent(self, event):
        self.position_thread.quit()
        self.position_thread.wait()
        event.accept()

def main(args=None):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
