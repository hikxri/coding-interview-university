class Queue:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size
        self.frontIndex = 0
        self.backIndex = -1

    def incrementFrontIndex(self):
        self.frontIndex += 1
        if self.frontIndex >= self.size:
            self.frontIndex -= self.size

    def incrementBackIndex(self):
        self.backIndex += 1
        if self.backIndex >= self.size:
            self.backIndex -= self.size

    def isEmpty(self):
        return self.data[self.frontIndex] is None

    def isFull(self):
        for item in self.data:
            if item is None:
                return False
        return True

    def enqueue(self, value):
        if not self.isFull():
            self.incrementBackIndex()
            self.data[self.backIndex] = value
        else:
            raise Exception("Queue is full.")

    def dequeue(self):
        if self.isEmpty():
            return None
        value = self.data[self.frontIndex]
        self.data[self.frontIndex] = None
        self.incrementFrontIndex()
        return value


if __name__ == "__main__":
    myQueue = Queue(5)
    print(myQueue.isEmpty(), myQueue.isFull())
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    print(myQueue.isEmpty(), myQueue.isFull())
    print(myQueue.dequeue())
    print(myQueue.data)
    myQueue.enqueue(4)
    myQueue.enqueue(5)
    myQueue.enqueue(6)
    print(myQueue.data)
    print(myQueue.dequeue())
    print(myQueue.dequeue())
    print(myQueue.dequeue())
    print(myQueue.data)
    print(myQueue.dequeue())
    print(myQueue.dequeue())
    print(myQueue.isEmpty(), myQueue.isFull())
