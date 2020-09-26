"""Print text in ASCII style

ASCII art allows you to represent forms by using characters.
To be precise, in our case, these forms are words.
For example, the word "MANHATTAN" could be displayed as follows in ASCII art:

# #  #  ### # #  #  ### ###  #  ###
### # # # # # # # #  #   #  # # # #
### ### # # ### ###  #   #  ### # #
# # # # # # # # # #  #   #  # # # #
# # # # # # # # # #  #   #  # # # #

​Your mission is to write a program that can display a line of text in ASCII
art in a style you are given as input.

Sample Input:
4
5
MANHATTAN

Sample Output:
# #  #  ### # #  #  ### ###  #  ###
### # # # # # # # #  #   #  # # # #
### ### # # ### ###  #   #  ### # #
# # # # # # # # # #  #   #  # # # #
# # # # # # # # # #  #   #  # # # #
"""
import string

width_of_character = int(input())
height_of_character = int(input())
text_to_print = input()

ascii_letters = {alphabet: [] for alphabet in string.ascii_uppercase + '?'}

for _ in range(height_of_character):
  characters_input = input()
  characters = [characters_input[i:i + width_of_character]
                for i in range(0, len(characters_input), width_of_character)]
  for (index, alphabet) in enumerate(string.ascii_uppercase + '?'):
    ascii_letters[alphabet].append(characters[index])

ascii_art = []
for i in range(height_of_character):
  ascii_art.append(''.join(
      ascii_letters[character.upper()][i]
      if character.upper() in ascii_letters else ascii_letters['?'][i]
    for character in text_to_print))

print('\n'.join(ascii_art))
