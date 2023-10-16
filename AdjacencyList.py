"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        if self.n - 1 < i < 0 or self.n - 1 < j < 0:
            raise IndexError
        if j in self.adj[i]:
            return
        self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        if self.n - 1 < i < 0 or self.n - 1 < j < 0:
            raise IndexError
        for k in range(len(self.adj[i])):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        if j in self.adj[i]:
            return True
        else:
            return False

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, j) -> List:
        indices = ArrayList.ArrayList()
        for k in range(self.n):
            if j in self.adj[k]:
                indices.append(k)
        return indices

    def size(self) -> int:
        return self.n

    def bfs(self, r : int):
        traversal = ArrayList.ArrayList()
        seen = np.zeros(self.n, dtype=bool)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        traversal.append(r)
        seen[r] = True
        while q.n > 0:
            current = q.remove()
            neighbors = self.out_edges(current)
            for neighbor in neighbors:
                if not seen[neighbor]:
                    q.add(neighbor)
                    traversal.append(neighbor)
                    seen[neighbor] = True
        return traversal

    def dfs(self, r : int):
        traversal = ArrayList.ArrayList()
        s = ArrayStack.ArrayStack()
        seen = np.zeros(self.n, dtype=bool)
        s.push(r)
        while s.n > 0:
            current = s.pop()
            if not seen[current]:
                traversal.append(current)
                seen[current] = True
            neighbors = self.out_edges(current)
            for k in range(neighbors.n - 1, -1, -1):
                if not seen[neighbors[k]]:
                    s.push(neighbors[k])
        return traversal


    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s
