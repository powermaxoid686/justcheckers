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

from collections import namedtuple

from enum import Enum

from justcheckers.game import rules

Point = namedtuple('Point', ['x', 'y'])


class GameState(Enum):
    NOT_STARTED = 0
    LIGHT_MOVE = 1
    DARK_MOVE = 2
    LIGHT_VICTORY = 3
    DARK_VICTORY = 4
    DRAW = 5


class Game(object):
    """
    Handles the logic behind the main game loop.

    :author: Ross Etchells
    :author: Dorian Pula
    """

    def __init__(self, light_player,
                 dark_player,
                 game_board=None,
                 game_rules=rules.CheckersVariant.American,
                 game_state=GameState.NOT_STARTED):
        """
        Initializes a new checker game

        :param light_player: The attack player.
        :param dark_player: The defending player.
        :param game_board: The checkerboard to use for the game.
        :param game_rules: The set of rules to use.
        :param game_state: The state of the game.
        :return: A representation of the game board.
        """

        self.light_player = light_player
        self.dark_player = dark_player
        self.board = game_board

        # TODO Initialize the rulebooks
        self.rules = game_rules
        self.state = game_state

    def is_light_player_turn(self):
        """
        Gets if it is the light player's turn. Returns false if it is the dark player's turn.

        :returns: True if it is the light player's turn. Returns false if it is the dark player's turn.
        """
        return self.state in [GameState.LIGHT_MOVE, GameState.LIGHT_VICTORY]
