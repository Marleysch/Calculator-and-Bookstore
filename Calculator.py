#import numpy as np
#import ArrayStack
import BinaryTree
import ChainedHashTable
#import DLList
import operator
import re


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable()

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        a = 0
        b = 0
        for char in s:
            if char == '(':
                a += 1
            if char == ')':
                b += 1
        if a == b:
            return True
        else:
            return False

    def _build_parse_tree(self, exp: str) -> str:
        if self.matched_expression(exp) is False:
            raise ValueError
        t = BinaryTree.BinaryTree()
        root = BinaryTree.BinaryTree.Node()
        t.r = root
        current = t.r
        for token in exp:
            if token == '(':
                current.insert_left(BinaryTree.BinaryTree.Node())
                current = current.left
            elif token == '+' or '-' or '/' or '*':
                current.set_val(token)
                current.set_key(token)
                current.insert_right(BinaryTree.BinaryTree.Node())
                current = current.right
            elif token == ')':
                current = current.parent
            else:
                current.set_key(token)
                current.set_val(self.dict.find(token))
                current = current.parent
        return t

    def _evaluate(self, u):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if u.left and u.right is not None:
            return self._evaluate(u.left) + op[u.k] + self._evaluate(u.right)
        elif u.left and u.right is None:
            if u.k is None:
                raise IndexError
            elif self.dict.find(u.k) is not None:
                return self.dict.find(u.k)
            else:
                return 'error'
        else:
            raise IndexError

    def evaluate(self, exp):
        parseTree = self._build_parse_tree(exp)
        return self._evaluate(parseTree.r)

    def print_expression(self, exp):
        variables = [x for x in re.split('\W+', exp) if x.isalnum()]
        everything_else = re.split('\w+', exp)
        if everything_else[0] == "''":
            for i in range(len(variables)):
                var = variables[i]
                if var != '':
                    everything_else.insert(2 * i, self.dict.find(var))
        else:
            for i in range(len(variables)):
                var = variables[i]
                if var != '':
                    everything_else.insert((2 * i) + 1, self.dict.find(var))
        print(''.join(everything_else))

