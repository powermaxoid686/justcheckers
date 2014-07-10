import sys

from PySide.QtCore import QUrl
from PySide.QtGui import QApplication
from PySide.QtDeclarative import QDeclarativeView


def main():
    # Create app
    app = QApplication(sys.argv)

    # Setup the QML declartive view
    view = QDeclarativeView()
    menu_view_url = QUrl('menu_view.qml')
    view.setSource(menu_view_url)
    view.show()
    
    # Enter app loop
    app.exec_()
    sys.exit()

if __name__ == '__main__':
    main()

