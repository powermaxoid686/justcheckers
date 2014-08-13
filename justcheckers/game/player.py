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


class Player(object):
    """
    Manages the information of a single player.

    :author: Chris Bellini
    :author: Dorian Pula
    """

    def __init__(self, name='Unnamed Player', wins=0, losses=0, ties=0):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.ties = ties

    def total_games_played(self):
        return self.wins + self.losses + self.ties

	def __str__(self):
		return 'Name: {name} \n Games: Won {wins} \ Lost {losses} \ Tied {ties}'.format(
            name=self.name, wins=self.wins, losses=self.losses, ties=self.ties
        )
