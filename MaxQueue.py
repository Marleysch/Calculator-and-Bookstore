from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()  # NOTE: DLLDeque implements the Deque interface but also inherits all methods
        # from DLList

    def add(self, x : object):
        u = SLLQueue.Node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1

        if self.max_deque.n == 0:
            self.max_deque.add_first(x)
        else:
            for i in range(self.max_deque.n):
                value = self.max_deque.get(i)
                if value > x:
                    continue
                else:
                    for j in range(self.max_deque.n - i):
                        self.max_deque.remove_last()
                    self.max_deque.add_last(x)
                    return
            self.max_deque.add_last(x)

    def remove(self) -> object:
        if self.n == 0:
            raise IndexError()
        y = self.head.x
        self.head = self.head.next
        self.n -= 1

        if y == self.max_deque.get(0):
            self.max_deque.remove_first()

        return y


    def max(self):
        """
        returns the maximum element stored in the queue
        """
        return self.max_deque.get(0)




