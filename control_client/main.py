import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class ControlApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Device Control Panel")
        self.setGeometry(100, 100, 300, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.status_label = QLabel("Status: Unknown", self)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        self.btn_start = QPushButton("Start", self)
        self.btn_start.clicked.connect(self.start_device)
        layout.addWidget(self.btn_start)

        self.btn_stop = QPushButton("Stop", self)
        self.btn_stop.clicked.connect(self.stop_device)
        layout.addWidget(self.btn_stop)

        self.btn_restart = QPushButton("Restart", self)
        self.btn_restart.clicked.connect(self.restart_device)
        layout.addWidget(self.btn_restart)

        self.setLayout(layout)

    def start_device(self):
        self.status_label.setText("Status: Running")
        print("Device started")

    def stop_device(self):
        self.status_label.setText("Status: Stopped")
        print("Device stopped")

    def restart_device(self):
        self.status_label.setText("Status: Restarting...")
        print("Device restarting...")
        # Simulasi restart delay (optional)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ControlApp()
    window.show()
    sys.exit(app.exec())
