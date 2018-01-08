def get_nodes(graph):
    """
    Returns a sorted list of all nodes in a graph
    """
    nodes = []
    for i in graph:
        for j in i:
            if j not in nodes:
                nodes.append(j)
    nodes.sort()
    return nodes


def matrix_adjacency_directed(graph):
    """
    (list of lists) -> (list of lists)
    Returns the adjacency matrix of the graph
    """
    nodes = get_nodes(graph)
    matrix = []

    for i in nodes:
        row = []
        for j in nodes:
            if [i, j] in graph:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)

    return matrix


def matrix_adjacency_undirected(graph):
    """
    (list of lists) -> (list of lists)
    Returns the adjacency matrix of the graph
    """
    nodes = get_nodes(graph)
    matrix = []

    for i in nodes:
        row = []
        for j in nodes:
            if [i, j] in graph or [j, i] in graph:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def matrix_incidence_directed(graph):
    """
    (list of lists) -> (list of lists)
    Returns the matrix of incidence of the graph
    """
    nodes = get_nodes(graph)
    matrix = []

    for node in nodes:
        row = []
        for j in graph:
            if len(edge) > 1:
                if node == edge[0] and node == edge[1]:
                    row.append(2)
                elif node == edge[0]:
                    row.append(1)
                elif node == edge[1]:
                    row.append(-1)
                else:
                    row.append(0)
            else:
                row.append(0)

        matrix.append(row)

    return matrix


def matrix_incidence_undirected(graph):
    """
    (list of lists) -> (list of lists)
    Returns the matrix of incidence of the graph
    """
    matrix = []
    nodes = get_nodes(graph)

    for node in nodes:
        row = []
        for edge in graph:
            if node in edge and len(edge) > 1:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def cycle_Euler_undirected(graph):
    """
    (list of lists) -> (list)
    Checks if Euler cycle exists in an undirected graph
    Returns False if not
    Else returns the list of nodes the cycle goes through
    """
    matrix = matrix_adjacency_undirected(graph)

    for row in matrix:
        if sum(row) % 2 != 0:
            return "No Euler cycle"

    nodes = get_nodes(graph)

    def find_tour(u, G, tour):
        for [a, b] in (x for x in G if len(x) > 1):
            if a == u:
                G.remove([a, b])
                find_tour(b, G, tour)
            elif b == u:
                G.remove([a, b])
                find_tour(a, G, tour)
        tour.insert(0, u)

    tour = []
    i = 0

    while tour == [] or i == len(nodes) - 1:
        find_tour(nodes[i], graph, tour)
        i += 1

    return tour


def cycle_Euler_directed(graph):
    """
    (list of lists) -> (list)
    Checks if Euler cycle exists in a directed graph
    Returns False if not
    Else returns the list of nodes the cycle goes through
    """
    matrix = matrix_adjacency_directed(graph)
    nodes = get_nodes(graph)

    def find_tour(u, G, tour):
        for [a, b] in (x for x in G if len(x) > 1):
            if a == u:
                G.remove([a, b])
                find_tour(b, G, tour)
        tour.insert(0, u)

    tour = []
    i = 0
    while tour == [] or i == len(nodes) - 1:
        find_tour(nodes[i], graph, tour)
        i += 1
    return tour if tour and len(tour) == len(list(x for x in matrix if
                                                  sum(x) != 0)) + 1 else False


def cycle_Hamiltonian_undirected(graph):
    """
    (list of lists) -> (list)
    Checks if Hamiltonian cycle exists in an undirected graph
    Returns False if not
    Else returns the list of nodes the cycle goes through
    """
    def find_all_tours(graph, start, end, tour=[]):
        tour = tour + [start]
        if start == end:
            return [tour]
        if start not in nodes:
            return []
        tours = []
        for edge in graph:
            if edge[0] == start and edge[1] not in tour:
                newtours = find_all_tours(graph, edge[1], end, tour)
                for newtour in newtours:
                    tours.append(newtour)
        return tours

    cycles = []
    matrix = matrix_adjacency_undirected(graph)
    for node in matrix:
        if sum(node) == 0:
            return False

    nodes = get_nodes(graph)

    for startnode in nodes:
        for endnode in nodes:
            newtours = find_all_tours(graph, startnode, endnode)
            for tour in newtours:
                if len(tour) == len(nodes):
                    if [tour[0], tour[len(nodes) - 1]] in graph or\
                       [tour[len(nodes) - 1], tour[0]] in graph:
                        tour.append(tour[0])
                        return tour
    return False


def cycle_Hamiltonian_directed(graph):
    """
    (list of lists) -> (list)
    Checks if Hamiltonian cycle exists in an directed graph
    Returns False if not
    Else returns the list of nodes the cycle goes through
    """
    def find_all_tours(graph, start, end, tour=[]):
        tour = tour + [start]
        if start == end:
            return [tour]
        if start not in nodes:
            return []
        tours = []

        for edge in graph:
            if edge[0] == start and edge[1] not in tour:
                newtours = find_all_tours(graph, edge[1], end, tour)
                for newtour in newtours:
                    tours.append(newtour)

        return tours

    cycles = []
    endnodes, startnodes = [], []

    matrix = matrix_adjacency_undirected(graph)
    for node in matrix:
        if sum(node) == 0:
            return False

    nodes = get_nodes(graph)

    for startnode in nodes:
        for endnode in nodes:
            newtours = find_all_tours(graph, startnode, endnode)
            for tour in newtours:
                if len(tour) == len(nodes):
                    if [tour[len(nodes) - 1], tour[0]] in graph:
                        tour.append(tour[0])
                        return tour

    return False


def paint(graph, n):
    """
    Checks if a graph could be painted into n colours
    Returns False if it`s impossible
    Otherwise returns string with node and it`s colour
    """
    if n < 1:
        return False

    import random

    palette = ["#%06x" % random.randint(0, 0xFFFFFF) for i in range(n)]
    nodes = get_nodes(graph)
    matrix = matrix_adjacency_undirected(graph)
    colors = {}
    adjacents = []

    def adjacents_have_diff_colors(nodes, color):
        return all(color != colors.get(n) for n in nodes)

    for row in matrix:
        adjacents.append([])
        for node in row:
            if node != 0:
                adjacents[-1].append(nodes[row.index(node)])
                row[row.index(node)] = 0

    nodes = get_nodes(graph)

    for node in range(len(nodes)):
        found_color = False
        for colr in range(n):
            if adjacents_have_diff_colors(adjacents[node], colr):
                found_color = True
                colors[nodes[node]] = colr
                break

        if not found_color:
            return False

    color_str = "["
    for key in colors:
        color_str += "[" + str(key) + ", " + "{color: " + \
                     str(palette[colors[key]]) + "], "
    color_str = color_str[:-2] + "]"

    return color_str


def is_Bipartite(graph):
    """
    Checks if graph is bipartite(can be divided into 2 groups)
    Returns True if it is, otherwise False
    """
    if len(get_nodes(graph)) < 2:
        return False
    return True if paint(graph, 2) else False

#print(is_Bipartite([[1,2],[3,2]]))
#print(paint([[2,3], [1,2], [3,1], [2,3], [2,2],[3,2], [1,3], [4,1], [1,4], [4,4]], 3))
#print(matrix_incidence_uфndirected([[1,1], [2,3], [2,3], [3,1], [1,3], [4]]))
#print(cycle_Hamiltonian_directed(sorted([[1,2], [2,3],  [3,4], [4,5], [5,1]])))
#print(cycle_Hamiltonian_directed(sorted([[1,5], [5,3],  [3,2], [2,4], [4,1]])))
#print(cycle_Hamiltonian_undirected(sorted([[2,3], [1,2], [3,1], [2,3], [2,2],[3,2], [1,3], [4,1], [1,4], [4,4]])))
#print(matrix_incidence_undirected(sorted([[2,3], [1,2], [3,1], [2,3], [2,2],[3,2], [1,3], [4,1], [1,4], [4,4]])))
#print(sorted([[2,3], [1,2], [3,1], [2,3], [2,2],[3,2], [1,3], [4,1], [1,4], [4,4]]))
#print(matrix_adjacency_directed(sorted([[2,3], [1,2], [3,1], [2,3], [2,2],[3,2], [1,3], [4,1], [1,4], [4,4]])))
#print(cycle_Euler_undirected(sorted([[1,4], [1,5], [2,4], [2,5], [4,5], [5,1], [5,3], [4,3]] )))
#print(cycle_Euler_directed(sorted([[1,4], [1,5], [2,4], [2,5], [4,5], [5,1], [5,3], [4,3], [4,2]] )))
#print(cycle_Euler_directed(sorted([[1,2], [2,3],  [4,1]] )))
#print(cycle_Euler_directed(sorted([[1,2], [2,4],  [4,3], [3,5], [5,1]] )))
