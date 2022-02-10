import random

class Word:


    def __init__(self):
        self.word_list = ["Coach", "Apple", "Event", "Index", "Shift", "Berry", "Heart", "Paper", "Space", "Quote"]

    def pick_word(self):
        self.word = random.choice(self.word_list).upper()
        return self.word

    # def __len__(self):
    #     return len(self.word)
