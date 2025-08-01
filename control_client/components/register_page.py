from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class RegisterPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Password")

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register)

        layout.addWidget(QLabel("Register Page"))
        layout.addWidget(self.email_input)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def register(self):
        email = self.email_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        if not email or not username or not password:
            QMessageBox.warning(self, "Error", "All fields are required.")
            return

        # TODO: Call actual API
        QMessageBox.information(self, "Register", f"Registered user {username}")
