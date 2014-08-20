#
# Copyright (c) 2014 Dorian Pula <dorian.pula@amber-penguin-software.ca>
#
# justCheckers is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# justCheckers is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with justCheckers.  If not, see <http://www.gnu.org/licenses/>.
#
# Please share and enjoy!
#

from PySide import QtGui

from PySide.QtOpenGL import QGLWidget
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# TODO Borrowed from: http://biospud.blogspot.ca/2012/02/proof-of-concept-opengl-program-in.html
def override(interface_class):
    """
    Method to implement Java-like derived class method override annotation.
    Courtesy of mkorpela's answer at
    http://stackoverflow.com/questions/1167617/in-python-how-do-i-indicate-im-overriding-a-method
    """
    def override(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return override


# Install freeglut3 for the example.
class SphereTestGLWidget(QGLWidget):
    "GUI rectangle that displays a teapot"
    @override(QGLWidget)
    def initializeGL(self):
      "runs once, after OpenGL context is created"
      glEnable(GL_DEPTH_TEST)
      glClearColor(1,1,1,0) # white background
      glShadeModel(GL_SMOOTH)
      glEnable(GL_COLOR_MATERIAL)
      glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
      glMaterialfv(GL_FRONT, GL_SHININESS, [50.0])
      glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 1.0, 0.0])
      glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
      glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
      glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [1.0, 1.0, 1.0, 0.0])
      glEnable(GL_LIGHTING)
      glEnable(GL_LIGHT0)
      self.orientCamera()
      glutInit()
      gluLookAt(0, 0, -10, # camera
                0, 0, 0, # focus
                0, 1, 0) # up vector

    @override(QGLWidget)
    def paintGL(self):
        "runs every time an image update is needed"
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.paintTeapot()

    @override(QGLWidget)
    def resizeGL(self, w, h):
        "runs every time the window changes size"
        glViewport(0, 0, w, h)
        self.orientCamera()

    def orientCamera(self):
      "update projection matrix, especially when aspect ratio changes"
      glPushAttrib(GL_TRANSFORM_BIT) # remember current GL_MATRIX_MODE
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      gluPerspective (60.0, self.width()/float(self.height()), 1.0, 10.0)
      glPopAttrib() # restore GL_MATRIX_MODE

    def paintTeapot(self):
      glPushAttrib(GL_POLYGON_BIT) # remember current GL_FRONT_FACE indictor
      glFrontFace(GL_CW) # teapot polygon vertex order is opposite to modern convention
      glColor3f(0.2,0.2,0.5) # paint it blue
      glutSolidTeapot(3.0) # thank you GLUT tool kit
      glPopAttrib() # restore GL_FRONT_FACE


class GameBoardWidget(QGLWidget):
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)


class GameView(QtGui.QWidget):
    """Info viewer for the game's license, etc."""

    # TODO Setup functional testing with PySide.QtTest

    def __init__(self):
        super(GameView, self).__init__()
        self.setup_components()

    def setup_components(self):

        self.game_board = SphereTestGLWidget(self)

        exit_button = QtGui.QPushButton('Back to Menu', self)
        exit_button.setFixedHeight(50)
        exit_button.clicked.connect(self.switch_to_menu_view)

        widget_layout = QtGui.QVBoxLayout(self)
        widget_layout.addWidget(self.game_board)

        # TODO Add in number of captured pieces and whose turn it is.

        button_row = QtGui.QHBoxLayout(self)
        button_row.addWidget(exit_button)

        widget_layout.addLayout(button_row)

        self.setLayout(widget_layout)

    def switch_to_menu_view(self):
        self.parentWidget().setCurrentIndex(0)
