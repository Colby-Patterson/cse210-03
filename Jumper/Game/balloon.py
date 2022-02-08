import os
from Game.terminal_service import TerminalService
from Game.word import Word
class Balloon:
    

  def __init__(self):

    self._tries = 5
    self._guessed_letter = []
    self._is_playing = True
    self._balloon_image = TerminalService()
    self.word = Word()
    self._word_completetion = '_' * len(self.word)

  def check_letters(self):
    print(self._word_completetion)
    for i in range (0,len(self.word)):
      letter = self.word[i]
      if self.guess == letter:
        self._word_completetion[i] = self.guess
    if '_' not in self._word_completetion:
      return False
    else:
      return True

  def status(self):
    print(self._balloon_image.display_balloon(self._tries))
    print(self._word_completetion)

  
  def play(self):

    while self._is_playing == True and self._tries > 0:
      
      self.guess = input('Guess a letter [a-z]: ')
      self.guess = self.guess.lower()

      if self.guess == self.word:
        self._is_playing = False
      if len(self.guess) == 1 and self.guess in self.word:
        for i in range(0,len(self.word)):
          letter = self.word[i]
          if self.guess == letter:
            self._word_completetion[i] = self.guess
        if '_' not in self._word_completetion:
          self._is_playing = False