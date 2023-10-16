import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        if len(self.a) == 0:
            raise IndexError()
        x = random.randint(0, self.n - 1)
        while self.a[x] is None:
            x = random.randint(0, self.n - 1)
        self.j = x
        y = super().remove()
        self.a[(self.j - 1) % len(self.a)] = None
        return y
'''
a = RandomQueue()
a.add(1)
print(a)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
print(a)
print(a.remove())
print(a)
print(a.remove())
print(a)
print(a.remove())
print(a)
print(a.remove())
print(a)
print(a.remove())
'''