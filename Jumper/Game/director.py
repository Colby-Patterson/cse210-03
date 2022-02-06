from Game.balloon import Balloon
from Game.word import Word
from Game.terminal_service import TerminalService


class Director:

    def __int__(self):

        self._is_playing = True
        self._balloon = Balloon()
        self._word = Word()
        self._terminal_service = TerminalService()

    def start_game(self):

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):

        letter = input('Guess a letter [a-z]: ')

    def _do_updates():

