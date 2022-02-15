import random
from Game.balloon import Balloon
from Game.word import Word
from Game.terminal_service import TerminalService
import os

#This class creates instances of the Balloon, Word, and TerminalService classes.

class Director:

    def __init__(self):

        self._is_playing = True
        self._balloon = Balloon()
        self._word = Word()
        self._terminal_service = TerminalService()
        self._guess = ''

    #The start_game method calls the _get_inputs method    

    def start_game(self):

        self._get_inputs()

    #The _get_inputs method get the current status(image) of the Balloon object
    #It also calls the play method of the Balloon, which handles letter input and checking the letter against the current word

    def _get_inputs(self):

        self._balloon.status()
        self._balloon.play()