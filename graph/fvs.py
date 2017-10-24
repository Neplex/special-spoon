""" graph """

import random

from graph import *


def fvs1(graph, k, l):
    """ fvs1 """
    modif = False

    for v, e in graph.items():
        if v in e:
            remove_vertex(graph, v)
            l.append(v)
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
            break

    return k, modif


def reduce_graph(graph, k, l):
    """ reduce graph """
    modif = True

    while modif:
        k, modif = fvs1(graph, k, l)
        #print("FVS1",graph,k)
        if not modif:
            k, modif = fvs2(graph, k)
            #print("FVS2",graph,k)
        if not modif:
            k, modif = fvs3(graph, k)
            #print("FVS3",graph,k)
        if not modif:
            k, modif = fvs4(graph, k)
            #print("FVS4", graph,k)

    # FVS5 -> return "no-instance" compute in 'random_fvs'

    return k


def random_fvs(graph, k, l):
    """ random FVS """
    k = reduce_graph(graph, k, l)

    if k < 0:
        return False
    elif not len(graph):
        return True
    else:
        v, _ = random.choice(list(graph.items()))
        l.append(v)
        remove_vertex(graph, v)
        return random_fvs(graph, k - 1, l)

def repeat_random_fvs(graph, k):
    """ repeat random FVS """
    i = 0
    nb_step = 4**k
    yes_instance = False
    l = []

    while i < nb_step and not yes_instance:
        del l[:]
        import copy
        tmp_g = copy.deepcopy(graph)
        yes_instance = random_fvs(tmp_g, k, l)
        i += 1

    return yes_instance, l
