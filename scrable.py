"""
When playing Scrabble©, each player draws 7 letters and must find
a word that scores the most points using these letters.

A player doesn't necessarily have to make a 7-letter word;
the word can be shorter. The only constraint is that the word
must be made using the 7 letters which the player has drawn.

For example, with the letters  etaenhs, some possible
words are: ethane, hates, sane, ant.

Your objective is to find the word that scores the
most points using the available letters (1 to 7 letters).

https://www.codingame.com/ide/puzzle/scrabble
"""

LETTER_POINTS = {
    'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1, 't': 1, 'l': 1,
    's': 1, 'u': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 6, 'x': 6,
    'q': 10, 'z': 10,
}

def cal_word_score(word):
  return sum(LETTER_POINTS[letter] for letter in word)

def cal_possibility(word):
  available_letters = list(AVAILABLE_WORD)
  for letter in word:
    if letter in available_letters:
      available_letters.remove(letter)
    else:
      return -1
  return cal_word_score(word)

NUMBER_OF_WORDS = int(input())
dictionary = [input() for _ in range(NUMBER_OF_WORDS)]

AVAILABLE_WORD = input()

dictionary.sort(key = lambda word: cal_possibility(word), reverse = True)
print(dictionary[0])
