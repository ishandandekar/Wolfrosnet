class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LindkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def add(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
            self.size += 1
        else:
            self.head.next = self.tail = Node(item)
            self.size += 1

    def print_list(self):
        curr = self.head
        while True:
            print(curr.data, end="")
            curr = curr.next
            if curr is None:
                break
            else:
                print("->", end="")


def main():
    l = LindkedList()
    l.add(1)
    l.add(2)
    l.print_list()


if __name__ == '__main__':
    main()
