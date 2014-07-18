import os
import sys

from PySide.QtGui import QWidget, QApplication, QLabel, QPushButton, QDesktopWidget, QVBoxLayout


class MenuScreen(QWidget):
    # TODO Divide up into separate widgets for the window and its contents.
    # TODO Figure out testing mechanism for PySide UIs.

    def __init__(self, app):
        super(MenuScreen, self).__init__()
        self.setWindowTitle('justCheckers')
        self.setGeometry(300, 300, 800, 600)
        self.setup_components()
        self.app = app
        self.center()

    def setup_components(self):
        self.systemLabel = QLabel(self.get_system_info(), self)
        self.exitButton = QPushButton('Exit', self)
        self.exitButton.clicked.connect(self.exit_app)

        widget_layout = QVBoxLayout(self)
        widget_layout.addWidget(self.systemLabel)
        widget_layout.addStretch()
        widget_layout.addWidget(self.exitButton)
        widget_layout.addStretch()
        self.setLayout(widget_layout)

    @staticmethod
    def get_system_info():
        """Retrieve information about the system."""
        message = 'I am running on {os}.\n My screen is {height}x{width}'
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
        self.app.quit()


def main():
    # TODO Should be moved out into a separate module
    app = QApplication(sys.argv)
    view = MenuScreen(app)
    view.show()
    app.exec_()
    sys.exit(0)

if __name__ == '__main__':
    main()
