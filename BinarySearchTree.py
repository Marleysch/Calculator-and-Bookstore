from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0

    def add(self, key: object, value: object = None) -> bool:
        new_node = self.Node(key, value)
        parent = self._find_last(key)
        return self._add_child(parent, new_node)

    def find(self, key: object) -> object:
        node = self._find_eq(key)
        if node is None:
            return None
        return node.v

    def remove(self, key: object):
        u = self._find_eq(key)
        if u is None:
            raise ValueError
        value = u.v
        self._remove_node(u)
        return value

    def _find_eq(self, key: object) -> BinaryTree.Node:
        current = self.r
        while current is not None:
            if key < current.k:
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        return None

    def _find_last(self, key: object) -> BinaryTree.Node:
        current = self.r
        parent = None
        while current is not None:
            parent = current
            if key < current.k:
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        return parent

    def _add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        if p is None:
            self.r = u
        else:
            if u.k < p.k:
                p.left = u
            elif u.k > p.k:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True

    def _splice(self, u: BinaryTree.Node):
        if u.left is not None:
            child = u.left
        else:
            child = u.right
        if u == self.r:
            self.r = child
            p = None
        else:
            p = u.parent
            if p.left == u:
                p.left = child
            else:
                p.right = child
        if child is not None:
            child.parent = p
        self.n -= 1

    def _remove_node(self, u: BinaryTree.Node):
        if u.left is None or u.right is None:
            self._splice(u)
        else:
            w = u.right
            while w.left is not None:
                w = w.left
            u.k = w.k
            u.v = w.v
            self._splice(w)

    def clear(self):
        """
        empties this BinarySearchTree
        """
        self.r = None
        self.n = 0

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.k
            u = self.next_node(u)

    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left is not None:
            w = w.left
        return w

    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

    def get_node(self, key):
        current = self.r
        smallest = None
        while current is not None:
            if key < current.key:
                smallest = current
                current = current.left
            elif key > current.key:
                smallest = current
                current = current.right
            else:
                return current
        return smallest
