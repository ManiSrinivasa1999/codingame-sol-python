"""
Auto-generated code below aims at helping you parse
the standard input according to the problem statement.
"""

def search(elements, root_node, length):
  """
  Args:
    elements(dict): all given connections
    root_node(int): value of current root
    length(int): depth of root node in current graph
  """
  if root_node not in elements:
    depths.append(length)
    return
  for neighbour in elements[root_node]:
    search(elements, neighbour, length + 1)


n = int(input())  # the number of relationships of influence
all_elements = {}
influenced = []
for i in range(n):
  # x: a relationship of influence between two people (x influences y)
  x, y = [int(j) for j in input().split()]
  if x in all_elements:
    all_elements[x].add(y)
  else:
    all_elements[x] = set([y])
  influenced.append(y)

root_nodes = []
for influencer in all_elements:
  if influencer not in influenced:
    root_nodes.append(influencer)

depths = []
initial_length = 1
for node in root_nodes:
  search(all_elements, node, initial_length)
print(max(depths))
