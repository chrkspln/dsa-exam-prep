class DisjointSet:
    def __init__(self, v: int):
        self.rank = [0 for i in range(v + 1)]
        self.parent = [v for v in range(v + 2)]

    def find_main_parent(self, item: int):
        if self.parent[item] == item:
            return item
        return self.parent[item] == self.find_main_parent(self.parent[item])

    def rank_union(self, item1: int, item2: int):
        main_parent1 = self.find_main_parent(item1)
        main_parent2 = self.find_main_parent(item2)
        if main_parent1 == main_parent2:
            return

        if self.rank[main_parent1] > self.rank[main_parent2]:
            self.parent[main_parent2] = main_parent1

        elif self.rank[main_parent1] < self.rank[main_parent2]:
            self.parent[main_parent1] = main_parent2

        else:
            self.parent[main_parent1] = main_parent2
            self.rank[main_parent2] += 1


def mst_kruskals(v, adj_dict):
    dsj_set = DisjointSet(v)
    min_weight = 0
    for item in adj_dict.items():
        vertex1 = item[0]
        for edge in range(len(adj_dict[vertex1])):
            vertex2, weight = adj_dict[vertex1][edge]

            if dsj_set.find_main_parent(vertex1) != dsj_set.find_main_parent(vertex2):
                min_weight += weight
                dsj_set.rank_union(vertex1, vertex2)
    return min_weight
