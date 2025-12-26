class UnionFind:
    
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
    
    
    def find(self, x: int) -> int:
        
        if self.parent[x] != x:
            self.parent[x] =  self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, p1: int, p2: int):
        
        p1_representative = self.find(p1)
        
        p2_representative = self.find(p2)
        
        if p1_representative == p2_representative:
            return False

        if self.rank[p1_representative] > self.rank[p2_representative]:
            self.parent[p2_representative] = p1_representative
        elif self.rank[p1_representative] < self.rank[p2_representative]:
            self.parent[p1_representative] = p2_representative
        else:
            self.parent[p1_representative] = p2_representative
            self.rank[p2_representative] += 1
        
        return True
    
    
    def connected(self, p1, p2):
        # returns True if both points has the same representative otherwise False
        return self.find(p1) == self.find(p2)
        