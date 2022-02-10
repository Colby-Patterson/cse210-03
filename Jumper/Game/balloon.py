from Game.terminal_service import TerminalService
from Game.word import Word
class Balloon:
    

  def __init__(self):

    self._tries = 5
    self._guessed_letter = []
    self._is_playing = True
    self._balloon_image = TerminalService()
    self.word = Word()
    self._new_word = self.word.pick_word()
    self._word_completion = '_' * len(self._new_word)

  def status(self):
  
    print(self._word_completion)
    print(self._balloon_image.display_balloon(self._tries))

  
  def play(self):

    while self._is_playing and self._tries > 0:
      
      self.guess = input('Guess a letter [a-z]: ').upper()

      if len(self.guess) == 1 and self.guess.isalpha():
        if self.guess in self._guessed_letter:
          print('You already guessed that letter.')
        elif self.guess not in self._new_word:
          print('That letter is not in the word, sorry.')
          self._tries -= 1
          self._guessed_letter.append(self.guess)
        else:
          print('You guessed a letter!')
          self._guessed_letter.append(self.guess)
          word_as_list = list(self._word_completion)
          indices = [i for i, letter in enumerate(self._new_word) if letter == self.guess]
          for index in indices:
            word_as_list[index] = self.guess
          self._word_completion = "".join(word_as_list)
          if '_' not in self._word_completion:
            self._is_playing = False
      else:
        print('Not a valid guess.')
      print(self._word_completion)
      print(self._balloon_image.display_balloon(self._tries))