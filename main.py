#!/usr/bin/env python
""" MAIN """

import sys

import graph


def main():
    """ main """
    # TODO
    # read file in parameters
    # compute result

    if len(sys.argv) != 2:
        print "Usage: %s <filename>" % sys.argv[0]
        exit(2)

    try:
        g = graph.io.from_graph(sys.argv[1])
    except IOError:
        sys.exit("%s: file not exist" % sys.argv[1])
    except graph.io.ParseError:
        sys.exit("%s: not a valid graph file" % sys.argv[1])

    print g

if __name__ == '__main__':
    main()
