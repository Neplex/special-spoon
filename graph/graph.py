""" Graph manipulation """


def remove_vertex(graph, vertex):
    """ remove vertex from graph """
    for v in graph[vertex]:
        while vertex in graph[v]:
            graph[v].remove(vertex)
    graph.pop(vertex)
