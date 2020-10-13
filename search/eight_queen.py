"""
Solution to the 8 queens board
States
Operator
Goal Test
Path Cost
"""

def goal_test(state):
  """Returns if state is valid 8 queen configuration

  Args:
    state(set): set of positions of existing queens
  Returns:
    valid(bollean): wheather a valid configuration  or not
  """
  if len(state) != 8:
    return False
  for queen_position  in state:
    x, y = queen_position
    # row collision
    for row_index in range(x - 8, x + 8):
      if (row_index, y) in state and row_index != x:
        return False
    # col collision
    for col_index in range(y - 8, y + 8):
      if (col_index, y) in state and col_index != y:
        return False
    # diagnal collision
    for diff in range(-8, 8):
      if ((row_index + diff, col_index + diff) in state and
            (row_index + diff, col_index + diff) != (x, y)):
        return False
  return True

def operator(state):
  """Returns the positions where queens can be placed

  Args:
    state(set): set of positions of existing queens
  Returns:
    set_if_states(list<set>): the possible next states
  """
  set_of_states = []
  for row_index in range(8):
    for col_index in range(8):
      if (row_index, col_index) not in state:
        new_state = state.copy()
        new_state.add((row_index, col_index))
        set_of_states.append(new_state)
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
  checked.add(str(state))
  for node in operator(state):  # expansion
    if node not in checked:
      solution = general_search(node, checked, solution)
      break
  return solution

initial_state = set()
