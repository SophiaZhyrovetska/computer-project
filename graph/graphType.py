# A module to define types of the graph. Argument of function - list of lists,
# where each list is an edge.


def Nodes(lst):
    """
    Returns the list of the nodes.
    Use for DIRECTED and UNDIRECTED graphs.
    """
    return list({edge[i] for i in range(2) for edge in lst})


def selfLoops(lst):
    """
    Returns True if there are self loops in the graph
    Use for DIRECTED and UNDIRECTED graphs.
    """
    for edge in lst:
        if edge[0] == edge[1]:
            return True


def parallelEdges(lst):
    """
    Returns True if there are parallel edges in the graph, False otherwise.
    Use for DIRECTED and UNDIRECTED graphs.
    """
    unique = []
    for edge in lst:
        if set(edge) not in unique :
            unique.append(set(edge))
    if (len(unique) < len(lst)):
        return True
    else:
        return False


def isMulti(lst):
    """
    Returns True if the graph is Multi graph, False otherwise.
    Use only for UNDIRECTED graphs.
    """
    if selfLoops(lst) is not True and parallelEdges(lst) is True:
        return True
    else:
        return False


def isPseudo(lst):
    """
    Returns True if the graph is Pseudograph, False otherwise.
    Use only for UNDIRECTED graphs.
    """
    if selfLoops(lst) is True:
        return True
    else:
        return False


def isSimple(lst):
    """
    Returns True if the graph is Simple graph, False otherwise.
    Use only for UNDIRECTED graphs.
    """
    if selfLoops(lst) is not True and parallelEdges(lst) is not True:
        return True
    else:
        return False


def isComplete(lst):
    """
    Returns True if the graph is Complete graph, False otherwise.
    Use for DIRECTED and UNDIRECTED graphs.
    """
    n = len(Nodes(lst))
    if (isSimple(lst) is True) and (len(lst) == n * (n - 1) / 2):
        return True
    else:
        return False


def isCycle(lst):
    """
    Returns True if the graph is Cycle graph, False otherwise.
    Use only for UNDIRECTED graphs.
    """
    nodes = len(Nodes(lst))
    edges = [sorted(edge) for edge in lst]
    edges = sorted(edges, key=lambda x:x[0])
    if (nodes < 3) and (isSimple(lst) is False):
        return False
    elif (edges[0][0] != edges[1][0]) or (edges[0][1] != edges[2][0]) or (edges[1][1] != edges[-1][1]):
        return False
    else:
        if len(lst) == 3:
            return True
        else:
            for i in range(2, len(lst) - 1):
                if (lst[i][1] == lst[i + 1][0]):
                    return True



def isWheel(lst):
    """
    Returns True if the graph is a Wheel graph, False otherwise.
    Use only for UNDIRECTED graphs.
    """
    nodes = [edge[i] for i in range(2) for edge in lst]
    n = len(Nodes(lst))
    count = 0
    if (n < 4) or (isSimple(lst) is False):
        return False
    elif (len(lst) == 6) and (n == 4):
        for node in nodes:
            if nodes.count(node) == 3:
                count += 1
        if (count == n * 3):
                return True
        else:
                return False
    else:
        for node in nodes:
            if nodes.count(node) == 3:
                count += 1
            elif nodes.count(node) == n - 1 :
                count += n - 1
        if (count == (n-1) *(3 + (n-1))):
            return True
        else:
            return False


def isDirectedMulti(lst):
    """
    Returns True if a directed graph is a Multi graph, False otherwise.
    Use only for DIRECTED graphs.
    """
    if parallelEdges(lst) is True:
        return True
    else:
        return False



def isDirectedCycle(lst):
    """
    Returns True if a directed graph is a Cycle graph, False otherwise.
    Use only for DIRECTED graphs.
    """
    nodes = len(Nodes(lst))
    lst = sorted(lst, key=lambda x:x[0])
    for i in range(len(lst) - 1):
        if (nodes >= 3) and (lst[i][1] == lst[i + 1][0]) and (lst[-1][1] == lst[0][0]) and (isSimple(lst) is True):
            return True
        else:
            return False
