"""
short_path
"""


def goal(node):
    state = node["state"]
    for i in state:
        for j in i:
            if j == "mo1":
                return True
    return False


def path(visited, node):
    path = [node]
    while path[-1]["parent"]:
        path.append(visited[path[-1]["parent"]])
    return path


def possible_moves(node):
    """
    return the next possible moves from given state
    Args:
      node(dict):it contains state,parent
    """
    moves = []
    root_state = node["state"]
    conversion = [list(i) for i in root_state]
    for i in range(len(conversion)):
        for j in range(len(conversion[i])):
            if conversion[i][j] == "o1":
                conversion_copy = conversion[:]
                try:
                    if conversion_copy[i-1][j] == "o":  # top
                        conversion_copy = conversion[:]
                        conversion_copy[i-1][j], conversion_copy[i][j] = conversion_copy[i][j], conversion_copy[i-1][j]
                        conversions = tuple(tuple(i) for i in conversion_copy)
                        move = {}
                        move["state"] = conversions
                        move["parent"] = root_state
                        moves.append(move)
                except:
                    pass
                try:
                    if conversion_copy[i+1][j] == "o":  # bottom
                        conversion_copy = conversion[:]
                        conversion_copy[i+1][j], conversion_copy[i][j] = conversion_copy[i][j], conversion_copy[i+1][j]
                        conversions = tuple(tuple(i) for i in conversion_copy)
                        move = {}
                        move["state"] = conversions
                        move["parent"] = root_state
                        moves.append(move)
                except:
                    pass
                try:
                    if conversion_copy[i][j-1] == "o":  # left
                        conversion_copy = conversion[:]
                        conversion_copy[i][j -
                                           1], conversion_copy[i][j] = conversion_copy[i][j], conversion_copy[i][j-1]
                        conversions = tuple(tuple(i) for i in conversion_copy)
                        move = {}
                        move["state"] = conversions
                        move["parent"] = root_state
                        moves.append(move)
                except:
                    pass
                try:
                    if conversion_copy[i][j+1] == "o":  # right
                        conversion_copy = conversion[:]
                        conversion_copy[i][j +
                                           1], conversion_copy[i][j] = conversion_copy[i][j], conversion_copy[i][j+1]
                        conversions = tuple(tuple(i) for i in conversion_copy)
                        move = {}
                        move["state"] = conversions
                        move["parent"] = root_state
                        moves.append(move)
                except:
                    pass
                try:
                    if conversion_copy[i-1][j] == "m":  # top
                        conversion_copy = conversion[:]
                        conversion_copy[i -
                                        1][j], conversion_copy[i][j] = "mo1", "o"
                        conversions = tuple(tuple(i) for i in conversion_copy)
                        move = {}
                        move["state"] = conversions
                        move["parent"] = root_state
                        moves.append(move)
                except:
                    pass
                try:
                    if conversion_copy[i+1][j] == "m":  # bottom
                        conversion_copy = conversion[:]
                        conversion_copy[i +
                                        1][j], conversion_copy[i][j] = "mo1", "o"
                        conversions = tuple(tuple(i) for i in conversion_copy)
                        move = {}
                        move["state"] = conversions
                        move["parent"] = root_state
                        moves.append(move)
                except:
                    pass
                try:
                    if conversion_copy[i][j-1] == "m":  # left
                        conversion_copy = conversion[:]
                        conversion_copy[i][j -
                                           1], conversion_copy[i][j] = "mo1", "o"
                        conversions = tuple(tuple(i) for i in conversion_copy)
                        move = {}
                        move["state"] = conversions
                        move["parent"] = root_state
                        moves.append(move)
                except:
                    pass
                try:
                    if conversion_copy[i][j+1] == "m":  # right
                        conversion_copy = conversion[:]
                        conversion_copy[i][j +
                                           1], conversion_copy[i][j] = "mo1", "o"
                        conversions = tuple(tuple(i) for i in conversion_copy)
                        move = {}
                        move["state"] = conversions
                        move["parent"] = root_state
                        moves.append(move)
                except:
                    pass
    return moves


def search(visited, fringe):
    """
    returns the total path
    Args:
      visited(dict) ={game_map:{"state":game_map,"parent":none}}
      fringe(list)  = next expansions
    """
    while fringe:
        node = fringe[0]
        fringe = fringe[1:]
        visited[node["state"]] = node
        if goal(node):
            print(path(visited, node))
        next_moves = possible_moves(node)
        for move in next_moves:
            if move["state"] not in visited:
                fringe.append(move)


game_map = (("o", "o", "o"), ("m", "x", "o"), ("o", "o1", "o"))
node = {"state": game_map, "parent": None}
fringe = [node]
visited = {}
search(visited, fringe)
