class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        size = 0
        current_node = self.head
        while current_node is not None:
            size += 1
            current_node = current_node.next
        return size

    def isEmpty(self):
        return self.head is None

    def prepend(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def append(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def insert(self, data, index):
        node = Node(data)
        if index == 0:
            self.prepend(data)
        else:
            i = 0
            current_node = self.head
            while current_node is not None:
                if i == index - 1:
                    node.next = current_node.next
                    current_node.next = node
                    return
                current_node = current_node.next
                i += 1
            print("Index out of range.")

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def access(self, index):
        i = 0
        current_node = self.head
        while current_node is not None:
            if i == index:
                return current_node.data
            current_node = current_node.next
            i += 1
        return "Index out of range."

    def search(self, data):
        i = 0
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return i
            current_node = current_node.next
            i += 1
        return -1

    def remove(self, index):
        if index == 0:
            self.popFront()
            return
        if index == self.size() - 1:
            self.popBack()
            return
        i = 0
        current_node = self.head
        while current_node is not None:
            if i == index - 1:
                current_node.next = current_node.next.next
                current_node = current_node.next
                current_node.prev = current_node.prev.prev
                return
            current_node = current_node.next
            i += 1
        print("Index out of range.")

    def popFront(self):
        if self.isEmpty():
            return None
        value = self.head.data
        if self.head.next is None:
            self.head = self.head.next
            return value
        self.head = self.head.next
        self.head.prev = None
        return value

    def popBack(self):
        if self.isEmpty():
            return None
        value = self.tail.data
        if self.tail.prev is None:
            self.tail = self.tail.prev
            return value
        self.tail = self.tail.prev
        self.tail.next = None
        return value

    def peekFront(self):
        return self.head.data

    def peekBack(self):
        return self.tail.data


if __name__ == "__main__":
    myList = DoublyLinkedList()
    print(myList.isEmpty())
    myList.prepend("2")
    myList.prepend("1")
    myList.append("3")
    myList.append("4")
    myList.append("5")
    myList.remove(0)
    myList.traverse()
