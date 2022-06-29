class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key: str):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] == (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


def main():
    stock_prices = [['march 6', 310.0], ['march 7', 320.0], ['march 8', 346.0], [
        'march 9', 382.0], ['march 10', 256.0], ['march 11', 369.0]]
    t = HashTable()
    for i in stock_prices:
        t[i[0]] = i[1]

    print(t['march 7'])
    del t['march 6']
    print(t['march 6'])


if __name__ == '__main__':
    main()
