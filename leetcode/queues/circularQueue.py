class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [None] * k
        self.size = 0
        self.head = 0
        self.tail = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.tail] = value
        self.size += 1
        self.tail = (self.tail + 1) % self.k
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.head = (self.head + 1) % self.k
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.tail - 1]

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False
