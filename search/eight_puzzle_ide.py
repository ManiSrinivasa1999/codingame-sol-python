"""
Solution to the 8 puzzle block using Iterative deepening
"""


def path_cost(path):
  """Returns the cost of current path
  Args:
    path(list<dict>): list of states in the current path
  Return:
    cost(int): the cost of this path
  """
  return len(path)


def generate_path(goal_node, visited):
  """Returns the path leading to the goal node
  """
  goal_state = goal_node['state']
  path = [goal_state]
  while goal_node['parent']:
    path.append(goal_node['state'])
    goal_node = visited[goal_node['parent']]
  return path


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


def general_search(fringe, visited, limiting_depth):
  """Returns one solution for the given search node
  Args:
    fringe(list<dict>): Nodes to be explored
    visited(dict): all visited nodes
  Returns:
    solution(list<dict> || False): The action sequence leading to the goal state
      or failure of search
  """
  node_to_be_explored = fringe[0]
  node_state = node_to_be_explored['state']
  visited[node_state] = node_to_be_explored
  if goal_test(node_to_be_explored['state']):
    return generate_path(node_to_be_explored, visited)
  current_depth = node_to_be_explored['depth']
  if current_depth == limiting_depth:
    return False
  children = [
      {
          'state': child_state,
          'parent': node_state,
          'depth': current_depth + 1,
      }
      for child_state in operator(node_state)]
  for child in children:
    if child['state'] in visited:
      continue
    fringe_copy = [child] + fringe[1:]
    visited_copy = visited.copy()
    solution = general_search(fringe_copy, visited_copy, limiting_depth)
    if solution:
      return solution
    else:
      continue
  return False


root_node = {
  'state': (3, 2, 4, 1, 7, 6, 0, 8, 5),
  'parent': None,
  'depth': 0,
}
for depth in range(1, 32):
  solution_path = general_search([root_node], {}, depth)
  if solution_path:
    break
solution_path = solution_path[::-1]
for state in solution_path:
  for i in range(3):
    print(state[i * 3:i * 3 + 3])
  print('-' * 6)
  print('-' * 6)
