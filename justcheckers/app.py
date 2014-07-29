import os
import sys

from PySide.QtCore import QCoreApplication
from PySide.QtGui import QWidget, QApplication, QLabel, QPushButton, QDesktopWidget, QVBoxLayout


class MenuScreen(QWidget):
    # TODO Divide up into separate widgets for the window and its contents.
    # TODO Setup functional testing with PySide.QtTest

    def __init__(self):
        super(MenuScreen, self).__init__()
        self.setWindowTitle('justCheckers')
        self.setGeometry(300, 300, 800, 600)
        self.setup_components()
        self.center()

    def setup_components(self):
        """Setup the components that make up the widget."""
        print(self.get_system_info())
        self.exit_button = QPushButton('Exit', self)
        self.exit_button.clicked.connect(self.exit_app)

        widget_layout = QVBoxLayout(self)
        widget_layout.addStretch()
        widget_layout.addWidget(self.exit_button)
        widget_layout.addStretch()
        self.setLayout(widget_layout)

    @staticmethod
    def get_system_info():
        """Retrieve information about the system."""
        message = 'I am running on {os}.\nMy screen is {height}x{width}'
        geometry = QDesktopWidget().availableGeometry()
        os_sys = ' '.join(os.uname())
        return message.format(os=os_sys, height=geometry.height(), width=geometry.width())

    def center(self):
        """Centers the widget in the middle of the screen."""
        widget_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        widget_rectangle.moveCenter(center_point)
        self.move(widget_rectangle.topLeft())

    def exit_app(self):
        """Exits the application."""
        QCoreApplication.instance().exit()


def main():
    # TODO Should be moved out into a separate module
    app = QApplication(sys.argv)
    view = MenuScreen()
    view.show()
    app.exec_()
    sys.exit(0)

if __name__ == '__main__':
    main()
