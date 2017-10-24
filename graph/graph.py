""" Graph manipulation """


def remove_vertex(graph, vertex):
    """ remove vertex from graph """
    while vertex in graph[vertex]:
        graph[vertex].remove(vertex)
    for v in graph[vertex]:
        while vertex in graph[v]:
            graph[v].remove(vertex)
    del graph[vertex]
