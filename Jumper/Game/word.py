import random

class Word:
    def __init__(self):
        self.word = ["Coach", "Apple", "Event", "Index", "Shift"]

    def choose_word(self):
        word = random.choice(self.word)