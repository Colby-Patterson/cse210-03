import random

# This class create a list of word and then randomly chooses a word from that list and stores it in a variable
# that we call to use as the secret word for the player to guess
class Word:

    # Creates a list of words
    def __init__(self):
        self.word_list = ["Coach", "Apple", "Event", "Index", "Shift", "Berry", "Heart", "Paper", "Space", "Quote"]

    # picks a word from the list of words above and returns it
    def pick_word(self):
        self.word = random.choice(self.word_list).upper()
        return self.word