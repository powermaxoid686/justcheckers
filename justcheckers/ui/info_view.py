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

import codecs

import markdown
from PySide import QtGui
from PySide import QtWebKit

from justcheckers.ui import util


class InfoView(QtGui.QWidget):
    """Info viewer for the game's license, etc."""

    # TODO Setup functional testing with PySide.QtTest

    def __init__(self):
        super(InfoView, self).__init__()
        self.setup_components()

    def setup_components(self):

        self.info_viewer = QtWebKit.QWebView(self)
        about_html = self.generate_html_from_markdown('credits.md')
        self.info_viewer.setHtml(about_html)

        exit_button = QtGui.QPushButton('Back to Menu', self)
        exit_button.setFixedHeight(50)
        exit_button.clicked.connect(self.switch_to_menu_view)

        credits_button = QtGui.QPushButton('Credits', self)
        credits_button.setFixedHeight(50)
        credits_button.clicked.connect(self.display_about_info)

        license_button = QtGui.QPushButton('License', self)
        license_button.setFixedHeight(50)
        license_button.clicked.connect(self.display_license_info)

        widget_layout = QtGui.QVBoxLayout(self)
        widget_layout.addWidget(self.info_viewer)

        button_row = QtGui.QHBoxLayout(self)
        button_row.addWidget(exit_button)
        button_row.addWidget(credits_button)
        button_row.addWidget(license_button)

        widget_layout.addLayout(button_row)

        self.setLayout(widget_layout)

    def switch_to_menu_view(self):
        self.parentWidget().setCurrentIndex(0)

    def display_about_info(self):
        about_html = self.generate_html_from_markdown('credits.md')
        self.info_viewer.setHtml(about_html)

    def display_license_info(self):
        license_html = self.generate_html_from_markdown('license.md')
        self.info_viewer.setHtml(license_html)

    def generate_html_from_markdown(self, filename):
        file_path = util.path_to_asset(filename, asset_type=util.TEXT_ASSETS)
        with codecs.open(file_path, mode='r', encoding='utf-8') as markdown_file:
            text = markdown_file.read()
        return markdown.markdown(text)

