import sys

sys.setrecursionlimit(10**5) 

input = lambda: sys.stdin.readline().rstrip()

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if root_a < root_b:
                self.parent[root_b] = root_a
            else:
                self.parent[root_a] = root_b
            return True
        return False

class Kruskal:
    def __init__(self, V, node):
        self.V = V
        self.node = sorted(node, key=lambda arr: arr[2]) # arr[2]: node_cost
        self.union_find = UnionFind(V)
        self.min_cost = 0

    def mst(self):
        for u, v, cost in self.node:
            if self.union_find.union(u, v):
                self.min_cost += cost
        return self.min_cost

V, E = map(int, input().split())

node = []
for _ in range(E):
    A, B, C = map(int, input().split()) # C: node_cost
    node.append((A, B, C))

answer = Kruskal(V, node).mst()

print(answer)