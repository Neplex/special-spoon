""" graph """

import random

from graph import *


def fvs1(graph, k):
    """ fvs1 """
    modif = False

    for v, e in graph.items():
        while v in e:
            e.remove(v)
            k -= 1
            modif = True

    return k, modif


def fvs2(graph, k):
    """ fvs2 """
    modif = False
    for v, e in graph.items():
        for elem in e :
            while e.count(elem) > 2 :
                e.remove(elem)
                modif = True
    return k, modif


def fvs3(graph, k):
    """ fvs3 """
    modif = False
    for v, e in graph.items():
        if len(e) < 2 :
            if len(e) == 1 :
                graph[e[0]].remove(v)
            del graph[v]
            modif = True
    return k, modif


def fvs4(graph, k):
    """ fvs4 """
    modif = False

    for v, e in graph.items():
        if len(e) == 2:
            graph[e[0]][graph[e[0]].index(v)] = e[1]
            graph[e[1]][graph[e[1]].index(v)] = e[0]
            graph.pop(v)
            modif = True

    return k, modif


def reduce_graph(graph, k):
    """ reduce graph """
    new_g = graph
    modif = True

    while modif:
        k, modif = fvs1(new_g, k)
        if not modif:
            k, modif = fvs2(new_g, k)
        if not modif:
            k, modif = fvs3(new_g, k)
        if not modif:
            k, modif = fvs4(new_g, k)

    # FVS5 -> return "no-instance" compute in 'random_fvs'

    return new_g, k


def random_fvs(graph, k):
    """ random FVS """
    new_g, k = reduce_graph(graph, k)

    if k < 0:
        return False
    elif not len(new_g):
        return True
    else:
        v, _ = random.choice(list(new_g.items()))
        remove_vertex(new_g, v)
        random_fvs(new_g, k - 1)


def repeat_random_fvs(graph, k):
    """ repeat random FVS """

    i = 0
    nb_step = 4**k
    yes_instance = False

    while i < nb_step and not yes_instance:
        yes_instance = random_fvs(graph, k)
        i += 1

    return yes_instance
