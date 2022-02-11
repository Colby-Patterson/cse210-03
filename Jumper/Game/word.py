import random

class Word:


    def __init__(self):
        self.word_list = ["Coach", "Apple", "Event", "Index", "Shift"]

    def pick_word(self):
        self.word = random.choice(self.word_list).upper()
        return self.word