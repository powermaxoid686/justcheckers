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

from enum import Enum


class CheckersVariant(Enum):
    AMERICAN = 0
    INTERNATIONAL = 1
    BRAZILIAN = 2
    CANADIAN = 3
    POOL = 4
    SPANISH = 5
    RUSSIAN = 6
    ITALIAN = 7
    SUICIDE = 8
    GHANAIAN = 9


class Rules(object):
    """
    Abstraction of the rules for a game of checkers.

    The rules for a game of checkers. This class provides a reference object for
    a game of checkers. This helps deal with the number of variants of checkers.
    One of the goals of justCheckers is to provide the flexibility of choose
    between different kinds of checker variants. This class builds a skeleton of
    the rules by defining what setup, moves, jumps, victory conditions and
    special moves make up a particular variant of checkers.

    :author: Dorian Pula
    :author: Chris Bellini
    """

    # Victory conditions.
    # Victory achieved by capturing all enemy pieces. */
    CAPTURE_ALL_ENEMIES_VICTORY = 0

    # TODO: Implement special rules for these checkers. Version >0.3?
    # Victory achieved by capturing all pieces. Only caveat is the three king
    # * versus one king draw rule:
    # *
    # * In many games at the end one adversary has three kings while the other
    # * one has just one king. In such a case the first adversary must win in
    # * thirteen moves or the game is declared a draw. (Shamelessly stolen from
    # * http://en.wikipedia.org/wiki/Draughts).
    # */
    SPECIAL_POOL_VICTORY = 1
    # Victory achieved some bizarre manner. TODO: Figure out Russian checkers.
    SPECIAL_RUSSIAN_VICTORY = 2
    # Victory achieved by losing all your pieces.
    SPECIAL_SUICIDE_VICTORY = 3
    # Victory achieved by not being the first with one piece left.
    SPECIAL_GHANAIAN_VICTORY = 4

    # TODO Move out into individual implementing Rules.
    # Checker board sizes.
    # Using a "standard" American checkers board.
    STANDARD_BOARD_SIZE = 8

    def __init__(self,
                 variant,
                 board_size=STANDARD_BOARD_SIZE,
                 kings_jump_multiple_times=True,
                 pawns_jump_backward=True,
                 light_player_starts_first=True,
                 mirrored_board=False,
                 force_capture=True,
                 force_capture_maximum=True):

        self.checkers_variant = variant
        self.board_size = board_size

        self.can_kings_jump_multiple_times = kings_jump_multiple_times
        self.can_pawns_jump_backwards = pawns_jump_backward

        self.does_light_player_start_first = light_player_starts_first
        self.is_board_mirrored = mirrored_board
        self.is_player_forced_to_capture = force_capture
        self.is_player_forced_to_capture_maximum_possible = force_capture_maximum

    def is_player_victorious(self, player, game):
        # TODO Check if the player is victorious
        # TODO Implement me for the standard capture or block all opponent pieces.
        return False


class AmericanRules(Rules):
    def __init__(self):
        super(AmericanRules, self).__init__(
            variant=CheckersVariant.AMERICAN,
            kings_jump_multiple_times=False,
            pawns_jump_backward=False,
            light_player_starts_first=False,
            force_capture_maximum=False,
        )


class InternationalRules(Rules):
    INTERNATIONAL_BOARD_SIZE = 10

    def __init__(self):
        super(InternationalRules, self).__init__(
            variant=CheckersVariant.INTERNATIONAL,
            board_size=self.INTERNATIONAL_BOARD_SIZE,
        )


class BrazilianRules(Rules):
    def __init__(self):
        super(BrazilianRules, self).__init__(
            variant=CheckersVariant.BRAZILIAN,
        )


class CanadianRules(Rules):
    CANADIAN_BOARD_SIZE = 12

    def __init__(self):
        super(CanadianRules, self).__init__(
            variant=CheckersVariant.CANADIAN,
            board_size=self.CANADIAN_BOARD_SIZE,
            force_capture_maximum=False,
        )


class PoolRules(Rules):
    def __init__(self):
        super(PoolRules, self).__init__(
            variant=CheckersVariant.POOL,
            light_player_starts_first=False,
            force_capture_maximum=False,
        )

    def is_player_victorious(self, player, game):
        # TODO Check if the player is victorious
        # TODO Implement special rules for Pool checkers.
        return False


class SpanishRules(Rules):
    def __init__(self):
        super(SpanishRules, self).__init__(
            variant=CheckersVariant.SPANISH,
            pawns_jump_backward=False,
            mirrored_board=True,
        )


class RussianRules(Rules):
    # TODO: Needs special freshly-kinged-but-still-can-jump special rule.
    def __init__(self):
        super(RussianRules, self).__init__(
            variant=CheckersVariant.RUSSIAN,
            force_capture_maximum=False,
        )

    def is_player_victorious(self, player, game):
        # TODO Check if the player is victorious
        # TODO Implement special rules for Russian checkers.
        return False


class ItalianRules(Rules):
    def __init__(self):
        super(ItalianRules, self).__init__(
            variant=CheckersVariant.ITALIAN,
            pawns_jump_backward=False,
            mirrored_board=True,
        )
    # TODO: Special rule on must jump most number of kings per capture.
    # TODO: Special rule that pawns can't capture kings.


class SuicideRules(Rules):
    # TODO: Needs unconventional setup.
    def __init__(self):
        super(SuicideRules, self).__init__(
            variant=CheckersVariant.SUICIDE,
        )

    def is_player_victorious(self, player, game):
        # TODO Check if the player is victorious
        # TODO Implement special rules for suicide checkers.
        return False


class GhanaianRules(Rules):
    # TODO: Special forfeit king if passing up a king's capture opportunity.
    def __init__(self):
        super(GhanaianRules, self).__init__(
            variant=CheckersVariant.GHANAIAN,
            mirrored_board=True,
            force_capture_maximum=False,
        )

    def is_player_victorious(self, player, game):
        # TODO Check if the player is victorious
        # TODO Implement special rules for Ghanian checkers.
        return False
