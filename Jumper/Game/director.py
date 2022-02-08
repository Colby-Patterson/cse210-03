import random
from Game.balloon import Balloon
from Game.word import Word
from Game.terminal_service import TerminalService
import os


class Director:

    def __init__(self):

        self._is_playing = True
        self._balloon = Balloon()
        self._word = Word()
        self._terminal_service = TerminalService()
        self._guess = ''

    def start_game(self):

        while self._is_playing:
            self._get_inputs()
            # self._do_updates()
            # self._do_outputs()

    def _get_inputs(self):

        new_balloon = self._balloon.status()
        self._balloon.play()


    # def _do_updates(self):

        
    #     pass

    # def _do_outputs(self):

    #     pass