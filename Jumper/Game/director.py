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
<<<<<<< HEAD
        self._guess = ''
=======
>>>>>>> 57b9ab5317304e9807339dbf01d54904ac167da3

    def start_game(self):

        while self._is_playing:
            self._get_inputs()
<<<<<<< HEAD
            # self._do_updates()
            # self._do_outputs()
=======
            #self._do_updates()
            #self._do_outputs()
>>>>>>> 57b9ab5317304e9807339dbf01d54904ac167da3

    def _get_inputs(self):

        new_balloon = self._balloon.status()
        self._balloon.play()

<<<<<<< HEAD

    # def _do_updates(self):

        
    #     pass

    # def _do_outputs(self):

    #     pass
=======
    #def _do_updates():

        #pass
>>>>>>> 57b9ab5317304e9807339dbf01d54904ac167da3
