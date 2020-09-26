"""Calculates the nth line of conway sequence

Warning! This sequence can make you ill. The reasoning is simple but unusual: Read a line aloud whilst looking at the line above and you will notice that each line (except the first) makes ​​an inventory of the previous line.

1
1 1
2 1
1 2 1 1
1 1 1 2 2 1
3 1 2 2 1 1

This sequence refers to a technique used to encode ranges in order to compress identical values ​​without losing any information. This type of method is used, amongst others, to compress images.
"""


def run_length_encoder(message_to_encode):
  """Returns the run length encoding of the message

  Args:
    message(list): the input to encode

  Returns:
    encoding(list): The run length encoding in a list of tuples

  Eg:
    '10000111000011' -> [('1', 1), ('0', 4), ('1', 3), ('0', 4), ('1', 2)]
  """
  break_points = [0]
  for i in range(1, len(message_to_encode)):
    if message_to_encode[i] != message_to_encode[i - 1]:
      break_points.append(i)
  break_points.append(len(message_to_encode))
  encoded = [(message_to_encode[break_points[i - 1]], break_points[i] - break_points[i - 1])
             for i in range(1, len(break_points))]
  return encoded

starting_number = input()
line_number = int(input())

result = [starting_number]
for _ in range(line_number - 1):
  rl_encoded = run_length_encoder(result)
  new_result = []
  for character, count in rl_encoded:
    new_result.append(str(count))
    new_result.append(character)
  result = new_result

print(' '.join(result))
