"""Find minimum number of exits in the building
https://www.codingame.com/training/medium/battle-tower
"""

def operator(node, graph, marked):
  """Returns adjacent nodes of node of graph

  Args:
    node<int>: represents the room
    graph<dict>: contains info on adjacent rooms
    marked<set>: set of rooms already marked
  Returns:
    adjacent<set>: set of adjacent rooms
  """

  return graph[node]

def search(root_node, graph, marked, visited):
  """Returns adjacent nodes of node of graph

  Args:
    root_node<int>: room currently under inspection
    graph<dict>: contains info on adjacent rooms
    marked<set>: set of rooms already marked
    visited<set>: set of visited rooms
  Returns:
    adjacent<set>: set of adjacent rooms
  """
  if root_node in visited:
    return marked
  visited.add(root_node)
  adjacent_rooms = graph[root_node]
  need_to_mark_room = True
  for room in adjacent_rooms:
    if room in marked:
      need_to_mark_room = False
  if need_to_mark_room:
    marked.add(root_node)
    solutions = [search(room, graph, marked) for room in adjacent_rooms]
    best_solution = min(solutions, key=len)
  else:
    pass

number_of_cells = int(input())
graph = {}
for _ in range(number_of_cells):
  cell_id, number_corridors, *adjacent = input().split()
  cell_id = int(cell_id)
  adjacent = set(list(map(int, adjacent)))
  graph[cell_id] = adjacent
