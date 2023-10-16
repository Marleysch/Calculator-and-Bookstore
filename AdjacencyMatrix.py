from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""


class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i : int, j : int):
        if 0 <= i < self.n and 0 <= j < self.n:
            self.adj[i][j] = True
        return True

    def remove_edge(self, i : int, j : int):
        if 0 <= i < self.n and 0 <= j < self.n:
            if self.adj[i][j]:
                self.adj[i][j] = False
                return True
            else:
                return False

    def has_edge(self, i : int, j: int) -> bool:
        if 0 <= i < self.n and 0 <= j < self.n:
            if self.adj[i][j] == 1:
                return True
            else:
                return False

    def out_edges(self, i) -> List:
        indices = ArrayList.ArrayList()
        for j in range(self.n):
            if self.has_edge(i, j):
                indices.append(j)
        return indices

    def in_edges(self, j) -> List:
        indices = ArrayList.ArrayList()
        for i in range(self.n):
            if self.has_edge(i, j):
                indices.append(i)
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