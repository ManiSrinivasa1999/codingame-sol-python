"""
Solution to the Eight puzzle block
States
Operator
Goal Test
Path Cost
"""

def path_cost(path):
  """Returns the cost of current path

  Args:
    path(list<dict>): list of states in the current path
  Return:
    cost(int): the cost of this path
  """
  return len(path)

def goal_test(state):
  """Returns if state matches goal

  Args:
    state(tuple): tuple representing game board
  Returns:
    goal_match(boolean): True if state is goal
  """
  goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
  return goal_state == state

def operator(state):
  """Returns states possible after a move is made

  Args:
    state(tuple): tuple represting the game board
  Returns:
    set_of_states(tuple): tuple of the possible board states

  Example:
  (1, 2, 3, 4, 5, 0, 7, 8, 6) -> [
    (1, 2, 0, 4, 5, 3, 7, 8, 6),
    (1, 2, 3, 4, 5, 6, 7, 8, 0),
    (1, 2, 3, 4, 0, 5, 7, 8, 6),
  ]
  ]
  """
  blank_position = state.index(0)
  set_of_states = []
  swapping_positions = {
      0: [1, 3],
      1: [0, 2, 4],
      2: [1, 5],
      3: [0, 4, 6],
      4: [1, 3, 5, 7],
      5: [2, 4, 8],
      6: [3, 7],
      7: [4, 6, 8],
      8: [5, 7],
  }
  for new_position in swapping_positions[blank_position]:
    new_state = list(state)
    new_state[new_position] = state[blank_position]
    new_state[blank_position] = state[new_position]
    set_of_states.append(tuple(new_state))
  return set_of_states

def general_search(state, checked, solution):
  """Returns one solution for the given search node

  Args:
    search_node(dict): dict representing the initial state
  Returns:
    solution(list<dict>): The action sequence leading to the goal state
  """
  if solution and goal_test(solution[-1]):
    return solution
  print(state)
  solution.append(state)
  checked.add(state)
  for node in operator(state):  # expansion
    if node not in checked:
      solution = general_search(node, checked, solution)
      break
  return solution


general_search((1, 2, 3, 4, 5, 0, 7, 8, 6), set(), [])

goal_1 = '123456780'
goal_2 = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal_3 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
goal_4 = {
    (0, 0): 1,
    (0, 1): 2,
    (0, 2): 3,
    (1, 0): 4,
    (1, 1): 5,
    (1, 2): 6,
    (2, 0): 7,
    (2, 1): 8,
    (2, 2): 0,
}

