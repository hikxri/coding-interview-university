class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

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
        else:
            node.next = self.head
            self.head = node

    def append(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

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

    def searchKey(self, key):
        i = 0
        current_node = self.head
        while current_node is not None:
            if current_node.data[0] == key:
                return i
            current_node = current_node.next
            i += 1
        return -1

    def popFront(self):
        if self.isEmpty():
            return None
        value = self.head.data
        self.head = self.head.next
        return value

    def popBack(self):
        if self.isEmpty():
            return None
        if self.head.next is None:
            result = self.head
            self.head = None
            return result.data
        current_node = self.head
        prev_node = self.head
        while current_node.next is not None:
            prev_node = current_node
            current_node = current_node.next
        result = current_node
        prev_node.next = None
        return result.data

    def remove(self, index):
        if index == 0:
            self.popFront()
            return
        if index == self.size() - 1:
            self.popBack()
            return
        i = 0
        current_node = self.head
        while current_node.next is not None:
            if i == index - 1:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            i += 1
        print("Index out of range.")


if __name__ == "__main__":
    myList = SinglyLinkedList()
    print(myList.isEmpty())
    myList.prepend("2")
    myList.prepend("1")
    myList.append("3")
    myList.append("4")
    myList.append("5")
    # myList.insert("A", 4)
    # myList.traverse()
    print(myList.isEmpty())
    # print("Access:", myList.access(0))
    # print("Search:", myList.search("3"))
    myList.remove(6)
    myList.traverse()
