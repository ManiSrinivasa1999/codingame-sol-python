"""
Print the order of succession of the Royal family members
"""

def operator(node, info_graph):
  """Returns children of node ordered in age and gender

  Args:
    node(<str>): Name of person
    graph(<dict>): Information about person

  Returns:
    children(list<str>): List of children names
  """
  children = [(name, info_graph[name]['birth'], info_graph[name]['gender'])
                for name in info_graph if info_graph[name]['parent'] == node]
  children.sort(key=lambda info:info[1])
  children.sort(key=lambda info:info[2], reverse=True)
  names = [child[0] for child in children]
  return names

def search(node, graph_info):
  """Prints order of succession

  Args:
    root_node(<str>): person name
    graph(<dict>): Information about person
  """
  if (graph_info[node]['death'] == '-' and
      not graph_info[node]['religion'] == 'Catholic'):
    print(node)
  children = operator(node, graph_info)
  for child in children:
    search(child, graph_info)

n = int(input())
root_node = ''
graph = {}
for i in range(n):
  name, parent, birth, death, religion, gender = input().split()
  graph[name] = {
      'name': name,
      'parent': parent,
      'birth': int(birth),
      'death': death,
      'religion': religion,
      'gender': gender,
  }
  if parent == '-':
    root_node = name
search(root_node, graph)
