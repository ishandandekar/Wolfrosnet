from Stack import Stack


class Graph():
    def __init__(self) -> None:
        self.v = set()
        self.e = []

    def __repr__(self) -> str:
        return "\n".join([f"{v}:{self._neighbors(v)}" for v in self.v])

    def __str__(self) -> str:
        return repr(self)

    def add_vertex(self, vertex):
        if vertex not in self.v:
            self.v.add(vertex)
        else:
            print(f"{vertex} is already a vertex!")

    def add_relation(self, vertex, end, weight=0):
        if vertex not in self.v:
            self.v.add(vertex)
        if end not in self.v:
            self.v.add(end)
        self.e.append((vertex, end, weight))

    def _neighbors(self, vertex):
        if vertex in self.v:
            nbrs = []
            for edge in self.e:
                if edge[0] == vertex:
                    nbrs.append(edge[1])
            return nbrs
        return []

    def print_neighbors(self, vertex):
        nbrs = self._neighbors(vertex)
        if vertex in self.v:
            print(f"{vertex} --> {nbrs}")
        else:
            print(f"{vertex} is not a vertex!")

    def to_dict(self):
        return {v: self._neighbors(v) for v in self.v}

    @property
    def adjacency_matrix(self):
        matrix = [([0]*len(self.v)) for i in range(len(self.v))]
        for vert_index, vert_list in enumerate(matrix):
            nbrs = self._neighbors(vert_index)
            for edge_index, edge in enumerate(vert_list):
                if edge_index in nbrs:
                    vert_list[edge_index] = 1
        return matrix

    def get_path(self, start, end):
        path = []
        print(f"{start} and {end}")
        if start == end:
            return []
        while start != end:
            for edge in self.e:
                if edge[1] == end:
                    path.append(edge[1])
                    end = edge[1]
                    print(f"{start} and {end}")
                    break
        return path

    def depth_first_search(self, vertex):
        # visited_path=[]
        # stack=Stack()
        # nbrs=self._neighbors(vertex)
        # visited_path.append(vertex)
        # for nbr in nbrs:
        #     stack.push(nbr)
        pass


def main():
    g = Graph()
    g.add_relation(0, 1)
    g.add_relation(0, 2)
    g.add_relation(1, 2)
    g.add_relation(1, 3)
    g.add_relation(1, 4)
    g.add_relation(1, 5)
    g.add_relation(3, 6)
    print(g.get_path(0, 6))
    # g.print_neighbors(2)
    # print(g)
    # print(g.adjacency_matrix)


if __name__ == '__main__':
    main()
