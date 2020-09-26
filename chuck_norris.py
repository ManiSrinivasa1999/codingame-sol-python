"""
Binary with 0 and 1 is good, but binary with only 0,
or almost, is even better! Originally, this is a concept
designed by Chuck Norris to send so called unary messages.

Write a program that takes an incoming message as input
and displays as output the message encoded using Chuck Norris’ method.

https://www.codingame.com/ide/puzzle/chuck-norris

Sample input:

C

Sample output:

0 0 00 0000 0 00

"""

def run_length_encoder(message_encoding):
  break_points = [0]
  for i in range(1, len(message_encoding)):
    if message_encoding[i] != message_encoding[ i - 1 ]:
      break_points.append(i)
  break_points.append(len(message_encoding))
  encoded = [(message_encoding[break_points[i - 1]],
              break_points[i] - break_points[i - 1])
              for i in range(1, len(break_points))]
  return encoded
message = input()
binary_message = ''.join([bin(ord(character))[2:].zfill(7)
                        for character in message])
encoding = run_length_encoder(binary_message)
chuck_norris_encoding = ''
for character, length in encoding:
  chuck_norris_encoding += '0' if character == '1' else '00'
  chuck_norris_encoding += f' { length * "0"} '
print(chuck_norris_encoding[:-1])
