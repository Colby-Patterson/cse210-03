from Game.word import Word
class Balloon:
    

  def __int__(self):

    self._tires = 5
    self._guessed_letter = []
    self._is_playing = True

  
  def guesses(self):

    while self._is_playing == True and self._tries > 0:
      guess = input('Guess a letter [a-z]: ')
      guess = guess.lower()

      if guess == self.word:
        self._is_playing = False
      if len(guess) == 1 and guess in self.word:
        for i in range(0,len(self.word)):
          letter = self.word[i]

  def display_balloon(tries):
    stages = [ """
                        x
                       /|\
                       / \
                     
                     ^^^^^^^
                   """,
                   """
                       \ /
                        o
                       /|\
                       / \
                     
                     ^^^^^^^
                   """,
                   """
                      \   /
                       \ /
                        o
                       /|\
                       / \
                     
                     ^^^^^^^
                   """,
                   """
                       ___
                      \   /
                       \ /
                        o
                       /|\
                       / \
                     
                     ^^^^^^^
                   """,
                   """
                      /___\
                      \   /
                       \ /
                        o
                       /|\
                       / \
                     
                     ^^^^^^^
                   """,
                   """
                       ___
                      /___\
                      \   /
                       \ /
                        o
                       /|\
                       / \
                     
                     ^^^^^^^
                   """]
    return stages[tries]