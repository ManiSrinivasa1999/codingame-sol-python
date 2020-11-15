"""Solver for peg solitaire
"""
def next_state_lol(current_state, move):
  """Returns the next state when the move is applied to current state
  Args:
    current_state(list<list<str>>): Current state of board
    move(int, int, int, int): Current position and next position of marble
  Returns:
    next_state(list<list<str>>): Next state of the board after applying move
  """
  start_x, start_y, end_x, end_y = move
  current_state_copy = current_state[:]
  current_state_copy[end_x][end_y] = 'B'
  current_state_copy[start_x][start_y] = 'W'
  if start_x == end_x:  # vertical move
    if start_y < end_y:  # moving down
      current_state_copy[start_x][start_y + 1] = 'W'
    elif start_y > end_y: # moving up
      current_state_copy[start_x][start_y - 1] = 'W'
  elif start_y == end_y:  # horizontal move
    if start_x < end_x:  # moving right
      current_state_copy[start_x + 1][start_y] = 'W'
    elif start_x > end_x:  # moving left
      current_state_copy[start_x - 1][start_y] = 'W'
  return current_state_copy

def next_state_dict_board(current_state, move):
  """Returns the next state when the move is applied to current state
  Args:
    current_state(dict): Current state of board
    move(int, int, int, int): Current position and next position of marble
  Returns:
    next_state(dict): Next state of the board after applying move
  """
  start_x, start_y, end_x, end_y = move
  current_state_copy = current_state.copy()
  current_position = (start_x, start_y)
  next_position = (end_x, end_y)
  current_state_copy[current_position] = 'W'
  current_state_copy[next_position] = 'B'
  # (5, 3), (3, 3) - top (4, 3)
  # (1, 3), (3, 3) - down (2, 3)
  # (3, 5), (3, 3) - left (3, 4)
  # (3, 1), (3, 3) - right (3, 2)
  middle_position = ((start_x + end_x) // 2, (start_y + end_y) // 2)
  current_state_copy[middle_position] = 'W'
  return current_state_copy

def next_state_str_board(current_state, move):
  start_x, start_y, end_x, end_y = move
  current_state_copy = list(current_state)[:]
  # BBBWBBB - left -> BWWBBBB
  # BBBWBBB - right -> BBBBWWB
  if start_y == end_y:
    if start_x < end_x:
      current_state_copy[start_y] = (current_state_copy[start_y][:start_x]
                            + 'WWB' + current_state_copy[start_y][end_x + 1:])
    else:
      current_state_copy[start_y] = (current_state_copy[start_y][:end_x]
                            + 'BWW' + current_state_copy[start_y][start_x + 1:])
  # top

  # ##BBB## -> ##BBB##
  # BBBBBBB -> BBBBBBB
  # BBBWBBB -> BBBBBBB
  # BBBBBBB -> BBBWBBB
  # ##BBB## -> ##BWB##

  # bottom

  # ##BBB## -> ##BWB##
  # BBBBBBB -> BBBWBBB
  # BBBWBBB -> BBBBBBB
  # BBBBBBB -> BBBBBBB
  # ##BBB## -> ##BBB##
  else:
    current_state_copy[start_x] = (current_state_copy[start_x][:start_y]
                            + 'W' + current_state_copy[start_x][start_y + 1:])
    current_state_copy[end_x] = (current_state_copy[end_x][:start_y]
                          + 'B' + current_state_copy[end_x][start_y + 1:])
    current_state_copy[(start_x + end_x) // 2] = (current_state_copy[(start_x + end_x) // 2][:start_y]
                          + 'W' + current_state_copy[(start_x + end_x) // 2][start_y + 1:])
  return tuple(current_state_copy)

def possible_nodes(root_node):
  """Returns all possible states
  Args:
    root_node(dict): node to expand
  Returns:
    All child nodes
  """
  root_state = root_node['state']
  child_nodes = []
  for i in range(len(root_state)):
    for j in range(len(root_state[i])):
      try:
        if root_state[i][j] == 'W':
          # bottom
          if root_state[i + 1][j] == 'B' and root_state[i + 2][j] == 'B':
            next_state = next_state_str_board(root_state, (i + 2, j, i, j))
            next_node = {'state': next_state, 'parent': root_state}
            child_nodes.append(next_node)
          # top
          elif root_state[i - 1][j] == 'B' and root_state[i - 2][j] == 'B':
            next_state = next_state_str_board(root_state, (i - 2, j, i, j))
            next_node = {'state': next_state, 'parent': root_state}
            child_nodes.append(next_node)
          # left
          elif root_state[i][j - 1] == 'B' and root_state[i][j - 2] == 'B':
            next_state = next_state_str_board(root_state, (i, j - 2, i, j))
            next_node = {'state': next_state, 'parent': root_state}
            child_nodes.append(next_node)
          # right
          elif root_state[i][j + 1] == 'B' and root_state[i][j + 2] == 'B':
            next_state = next_state_str_board(root_state, (i, j + 2, i, j))
            next_node = {'state': next_state, 'parent': root_state}
            child_nodes.append(next_node)
      except:
        pass
  return child_nodes

def goal_state(state):
  """Returns wheather state is goal state
  Args:
    state(tuple): state in tuples
  Returns:
    boolean value
  """
  counter = 0
  for i in range(len(state)):
    for j in range(len(state[i])):
      if state[i][j] == 'B':
        counter += 1
  return counter == 1

def path(root_node, visted):
  paths = []
  while root_node['parent']:
    paths.append(root_node['state'])
    root_node = visted[root_node]['parent']
  return paths

def search(visited, update_fringe):
  while update_fringe:
    root_node = update_fringe[0]
    update_fringe = update_fringe[1:]
    if goal_state(root_node['state']):
      return path(root_node, visited)
    visited[root_node['state']] = root_node
    child_nodes = possible_nodes(root_node)
    for child_node in child_nodes:
      if child_node['state'] not in visited:
        update_fringe.append(child_node)


lol_board = [
    ['#', '#', 'B', 'B', 'B', '#', '#',],
    ['#', '#', 'B', 'B', 'B', '#', '#',],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B',],
    ['B', 'B', 'B', 'W', 'B', 'B', 'B',],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B',],
    ['#', '#', 'B', 'B', 'B', '#', '#',],
    ['#', '#', 'B', 'B', 'B', '#', '#',],
]
dict_board = {
  (0, 0): '#', (0, 1): '#', (0, 2): 'B',
  (0, 3): 'B', (0, 4): 'B', (0, 5): '#', (0, 6): '#',
  (1, 0): '#', (1, 1): '#', (1, 2): 'B',
  (1, 3): 'B', (1, 4): 'B', (1, 5): '#', (1, 6): '#',
  (2, 0): 'B', (2, 1): 'B', (2, 2): 'B',
  (2, 3): 'B', (2, 4): 'B', (2, 5): 'B', (2, 6): 'B',
  (3, 0): 'B', (3, 1): 'B', (3, 2): 'B',
  (3, 3): 'W', (3, 4): 'B', (3, 5): 'B', (3, 6): 'B',
  (4, 0): 'B', (4, 1): 'B', (4, 2): 'B',
  (4, 3): 'B', (4, 4): 'B', (4, 5): 'B', (4, 6): 'B',
  (5, 0): '#', (5, 1): '#', (5, 2): 'B',
  (5, 3): 'B', (5, 4): 'B', (5, 5): '#', (5, 6): '#',
  (6, 0): '#', (6, 1): '#', (6, 2): 'B',
  (6, 3): 'B', (6, 4): 'B', (6, 5): '#', (6, 6): '#',
}
string_board = (
    '##BBB##',
    '##BBB##',
    'BBBBBBB',
    'BBBWBBB',
    'BBBBBBB',
    '##BBB##',
    '##BBB##',
)
visted = {}
fringe = [{ 'state': string_board, 'parent': None}]
path = search(visted, fringe)
print(path)
