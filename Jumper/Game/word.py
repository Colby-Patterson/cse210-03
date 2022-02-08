import random

class Word:


    def __init__(self):
<<<<<<< HEAD
        self.word_list = ["Coach", "Apple", "Event", "Index", "Shift"]

    def pick_word(self):
        self.word = random.choice(self.word_list)
        return self.word

    # def __len__(self):
    #     return len(self.word)
=======
        self.word = random.choice(["Coach", "Apple", "Event", "Index", "Shift"])

    def __len__(self):
        return len(self.word)
>>>>>>> 57b9ab5317304e9807339dbf01d54904ac167da3
