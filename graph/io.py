""" Input/Output for graph """


class ParseError(Exception):
    '''raised when error occured during parse'''


def from_graph(path):
    """ Read graph from graph file """
    # TODO
    k = None
    d = {}
    with open(path) as graph_file:
        lines = graph_file.readlines()

        if len(lines) < 3:
            raise ParseError()

        try:
            k = int(lines[1])
            n = int(lines[2])
        except ValueError:
            raise ParseError()

        if n + 3 != len(lines):
            raise ParseError()

        for line in lines[3:]:
            v, e = line.split(':')
            #e = e.strip()[1:-2].split(', ')
            d[v] = list(e)

    return d, k


def to_dot(graph, path):
    """ To dot """
    import graphviz as gv
    dot = gv.Graph(format="png")
    for vertex, edges in graph.iteritems():
        dot.node(vertex)
        for edge in edges:
            dot.edge(vertex, edge)

    dot.render(filename=path)
