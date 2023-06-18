class Jar:
    def __init__(self,capacity=12):
        if capacity < 0:
            raise ValueError("Capacity can't be less than zero")

        self._capacity : int = capacity
        self._size: int = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if (self.capacity < n) or (self.size + n > self.capacity):
            raise ValueError("Capacity exceeded.")
        else:
            self._size += n

    def withdraw(self, n):
        if self.size < n:
             raise ValueError("Not enough cookies.")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size