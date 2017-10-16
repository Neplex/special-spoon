""" graph """


def fvs1(graph, k):
    """ fvs1 """
    for v, e in graph.items():
        while v in e:
            e.remove(v)
            k -= 1
    return k


def fvs2(graph, k):
    """ fvs2 """
    return k


def fvs3(graph, k):
    """ fvs3 """
    return k


def fvs4(graph, k):
    """ fvs4 """
    to_remove = []

    for v, e in graph.items():
        if len(e) == 2:
            graph[e[0]][graph[e[0]].index(v)] = e[1]
            graph[e[1]][graph[e[1]].index(v)] = e[0]
            to_remove.append(v)

    for v in to_remove:
        graph.pop(v)

    return k


def fvs5(graph, k):
    """ fvs5 """
    return k


def reduce_graph(graph, k):
    """ reduce graph """
    modif = True
    new_g = graph
    new_k = k

    while modif:
        modif = False

    return new_g, new_k


def random_fvs(graph, k):
    """ random FVS """
    new_g, new_k = reduce_graph(graph, k)

    if new_k < 0:
        return False
    elif new_g:  # new_g est vide
        return True
    else:
        pass


def repeat_random_fvs(graph):
    """ repeat random FVS """
    # TODO
    return False
