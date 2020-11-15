"""
Abalone Solution
"""
rows = 'abcefghi'
cols = [1, 2, 3, 4, 5, 6, 7, 8, 9]

abalone_board_dict = {}
for i, row in enumerate(rows):
  for j, col in enumerate(cols):
    abalone_board_dict[row + str(col)] = {
      'value': ' ',
      '1': rows[i + 1] + str(cols[j + 1])
        if i + 1 < len(rows) and j + 1 < len(cols) else '#',
      '2': row + str(cols[j + 1]) if j + 1 < len(rows) else '#',
      '3': rows[i - 1] + str(col) if i - 1 > 0 else '#',
      '4': rows[i - 1] + str(cols[j - 1]) if i - 1 >= 0 and j - 1 > 0 else '#',
      '5': row + str(cols[j - 1]) if j - 1 >= 0 else '#',
      '6': rows[i + 1] + str(col) if i + 1 < len(rows) else '#',
    }

for row in 'ab':
  for col in cols:
    abalone_board_dict[row + str(col)]['value'] = 'B'

for row in 'hi':
  for col in cols:
    abalone_board_dict[row + str(col)]['value'] = 'R'

for cell in ['c3', 'c4', 'c5']:
  abalone_board_dict[cell]['value'] = 'B'

for cell in ['g5', 'g6', 'g7']:
  abalone_board_dict[cell]['value'] = 'R'
