import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QMenuBar
from PyQt6.QtGui import QAction

from components.login_page import LoginPage
from components.register_page import RegisterPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agent Control Panel")
        self.setGeometry(100, 100, 400, 300)

        # Stacked widget untuk ganti halaman
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Tambah halaman ke stack
        self.login_page = LoginPage()
        self.register_page = RegisterPage()
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.register_page)

        # Menu
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)

        page_menu = menu_bar.addMenu("Menu")

        login_action = QAction("Login", self)
        register_action = QAction("Register", self)

        login_action.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(self.login_page))
        register_action.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(self.register_page))

        page_menu.addAction(login_action)
        page_menu.addAction(register_action)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
