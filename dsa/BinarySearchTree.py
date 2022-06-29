class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        new_val = Node(new_val)
        self._insert_value(self.root, new_val)

    def _insert_value(self, start, new_val):
        if start.left is None and new_val.value < start.value:
            start.left = new_val
        if start.right is None and new_val.value > start.value:
            start.right = new_val
        if start.left is not None and new_val.value < start.value:
            return self._insert_value(start.left, new_val)
        if start.right is not None and new_val.value < start.value:
            return self._insert_value(start.right, new_val)

    def search(self, find_val):
        return self._search(self.root, find_val)

    def _search(self, start, find_val):
        if start.value == find_val:
            return True
        if start.right is not None and find_val > start.value:
            self._search(start.right, find_val)
        if start.left is not None and find_val < start.value:
            print(f"{start.left} ------ {find_val}")
            self._search(start.left, find_val)
        return False


def main():
    # Set up tree
    tree = BST(4)

    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    # Check search
    # Should be True
    print(tree.search(4))
    # Should be False
    print(tree.search(6))


if __name__ == '__main__':
    main()
