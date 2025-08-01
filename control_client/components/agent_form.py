from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QMessageBox
import api

class AgentForm(QWidget):
    def __init__(self, table_ref):
        super().__init__()
        self.table_ref = table_ref

        layout = QHBoxLayout()
        self.hostname_input = QLineEdit()
        self.hostname_input.setPlaceholderText("Hostname")

        self.os_input = QLineEdit()
        self.os_input.setPlaceholderText("Operating System")

        self.add_btn = QPushButton("Add Agent")
        self.add_btn.clicked.connect(self.add_agent)

        layout.addWidget(self.hostname_input)
        layout.addWidget(self.os_input)
        layout.addWidget(self.add_btn)
        self.setLayout(layout)

    def add_agent(self):
        hostname = self.hostname_input.text()
        os = self.os_input.text()

        if not hostname or not os:
            QMessageBox.warning(self, "Input Error", "Hostname and OS are required.")
            return

        result = api.register_agent(hostname, os)
        QMessageBox.information(self, "Success", result["message"])

        self.hostname_input.clear()
        self.os_input.clear()
        self.table_ref.load_agents()
