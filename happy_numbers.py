"""
A happy number is defined by the following process:
Starting with any positive integer, replace the number by
the sum of the squares of its digits in base-ten, and repeat
the process until the number either equals 1 (where it will stay),
or it loops endlessly in a cycle that does not include 1.
Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers.

Given a list of numbers, classify each of them as happy or unhappy.

https://www.codingame.com/ide/puzzle/happy-numbers
"""
def is_happy(number):
  computed_sums = set([])
  computed_sum = sum([int(digit)** 2 for digit in number])
  number = str(computed_sum)
  while computed_sum not in computed_sums or len(number) != 1:
    computed_sums.add(computed_sum)
    computed_sum = sum([int(digit)** 2 for digit in number])
    number = str(computed_sum)
  return number == '1'

number_of_inputs = int(input())
for _ in range(number_of_inputs):
  input_number = input()
  number_is_happy = is_happy(input_number)
  if number_is_happy:
    print(input_number, ':)')
  else:
    print(input_number, ':(')
