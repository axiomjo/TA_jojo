from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from robot_interface import RobotInterface
from PyQt5.QtCore import QTimer


class MyCobotWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyCobot 280 Pi Controller")
        self.interface = RobotInterface()

        self.layout = QVBoxLayout()

        self.coord_label = QLabel("End-Effector: Loading...")
        self.joint_label = QLabel("Joints: Loading...")
        self.warning_label = QLabel("")
        self.warning_label.setStyleSheet("color: red")

        self.layout.addWidget(self.coord_label)
        self.layout.addWidget(self.joint_label)
        self.layout.addWidget(self.warning_label)

        # Increment buttons
        self.add_movement_buttons()

        self.setLayout(self.layout)

        # Update info every 500ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_info)
        self.timer.start(500)

    def add_movement_buttons(self):
        directions = ["+X", "-X", "+Y", "-Y", "+Z", "-Z"]
        for dir in directions:
            btn = QPushButton(f"Move {dir}")
            btn.clicked.connect(lambda checked, d=dir: self.move(d))
            self.layout.addWidget(btn)

    def move(self, direction):
        success, warning = self.interface.incremental_move(direction)
        self.warning_label.setText(warning if not success else "")

    def update_info(self):
        pos = self.interface.get_end_effector_coords()
        joints = self.interface.get_joint_angles()
        self.coord_label.setText(f"End-Effector: {pos}")
        self.joint_label.setText(f"Joints: {joints}")
