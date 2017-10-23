""" Input/Output for graph """
import re


class ParseError(Exception):
    '''raised when error occured during parse'''


def from_graph(path):
    """ Read graph from graph file """
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
            if re.match(r"[0-9]* *: *\[ *[0-9]* *(, *[0-9]* *)*\]", line) is None:
                raise ParseError()
            v, e = line.split(':')
            for car in "[] \n":
                e = e.replace(car, "")
            v = v.strip(" ")
            d[v] = e.split(",")

    return d, k


def to_dot(graph, path):
    """ To dot """
    import graphviz as gv
    dot = gv.Digraph(format="png")
    for vertex, edges in graph.iteritems():
        dot.node(vertex)
        for edge in edges:
            dot.edge(vertex, edge)

    dot.render(filename=path)
