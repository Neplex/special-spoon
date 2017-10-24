#!/usr/bin/env python
""" MAIN """

import sys

import graph


def main():
    """ main """

    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        exit(2)

    try:
        g, k = graph.io.from_graph(sys.argv[1])
        if len(sys.argv) > 2:
            graph.io.to_dot(g, sys.argv[2])
    except IOError:
        sys.exit("%s: file not exist" % sys.argv[1])
    except graph.io.ParseError:
        sys.exit("%s: not a valid graph file" % sys.argv[1])

    res,coupe = graph.fvs.repeat_random_fvs(g, k)

    if res :
        print("yes")
        print(coupe)
    else:
        print("no")

if __name__ == '__main__':
    main()
