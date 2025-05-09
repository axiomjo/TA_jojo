from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import QRect

app = QApplication([])
button = QPushButton("Click Me")
button.setGeometry(QRect(50, 50, 100, 30))
button.show()

def get_button_position():
    rect = button.geometry()
    button_info = {
        "x_screen": rect.x(),
        "y_screen": rect.y(),
        "width": rect.width(),
        "height": rect.height()
    }
    print(button_info)

get_position_button = QPushButton("Get Position")
get_position_button.clicked.connect(get_button_position)
get_position_button.show()

app.exec_()
