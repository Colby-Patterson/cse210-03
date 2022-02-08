import random

class Word:
    def __init__(self):
        self.word = random.choice(["Coach", "Apple", "Event", "Index", "Shift"])

    def __len__(self):
        return len(self.word)