#!/usr/bin/env python3

import sys


class Graph(object):

    def __init__(self, V):
        self.V = V
        self.adj = {}
        for v in range(V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)


class BFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.marked = [False for _ in range(g.V)]
        self.parent = [False for _ in range(g.V)]
        self.bfs(s)

    def bfs(self, s):
        queue = [s]
        self.marked[s] = True

        while queue:
            v = queue.pop(0)
            for w in self.g.adj[v]:
                if not self.marked[w]:
                    queue.append(w)
                    self.parent[w] = v
                    self.marked[w] = True

    # Return True if there is a path from s to v
    def hasPathTo(self, v):
        return self.marked[v]

    # Return path from s to v (or None should one not exist)
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = [v]
        while v != self.s:
            v = self.parent[v]
            path.append(v)
        return path[::-1]


def main():
    with open(sys.argv[1]) as f:
        V = int(f.readline())
        g = Graph(V)

        for line in f:
            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    toPrint = []
    paths = BFSPaths(g, int(sys.argv[2]))
    for i in range(0, V):
        if len(paths.pathTo(i)) <= int(sys.argv[3]) + 1:
            toPrint.append(i)

    print(toPrint)


if __name__ == '__main__':
    main()
