from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < self.n / 2:
            p = self.dummy.next
            for j in range(i):
                p = p.next
        else:
            p = self.dummy
            for j in range(self.n - i):
                p = p.prev
        return p

    def get(self, i) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        u = self.get_node(i)
        return u.x

    def set(self, i: int, x: object) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        node = self.get_node(i)
        old = node.x
        node.x = x
        return old

    def add_before(self, w: Node, x: object) -> Node:
        if w is None:
            return IndexError()
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        w.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i: int, x: object):
        if i < 0 or i > self.n:
            raise IndexError()
        return self.add_before(self.get_node(i), x)

    def remove(self, i: int):
        if i < 0 or i >= self.n:
            raise IndexError()
        w = self.get_node(i)
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:
        for i in range(self.n - 1):
            if (self.get(i)).lower() == (self.get(self.n - 1 - i)).lower():
                continue
            else:
                return False
        return True

    def reverse(self):
        u = self.dummy
        for i in range(self.n + 1):
            temp = u.next
            u.next = u.prev
            u.prev = temp
            u = u.next

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + ']'

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
