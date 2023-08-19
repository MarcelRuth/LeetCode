# Creating Class For MST Algorithm
class UnionFind:
    def __init__ (self, n):
        self.parents = list(range(n))  # Initialy Every Vertex Is It's Own Parent
        self.weight = 0                # Initialy Weight = 0
        self.edgeCount = 0             # Initialy edgeCount = 0

    def find(self, x):                 # Find Function TO Find The Parent Of X Recursively
        if x != self.parents[x]:       # If X is not it's Own Parent
            self.parents[x] = self.find(self.parents[x])    # then Finding It's Parent
        return self.parents[x]         # Returning The Parent Of X

    def union(self, x, y, w):          # Union Function TO Creating MST Algo
        r1 = self.find(x)              # Finding The X Parent
        r2 = self.find(y)              # Finding The Y Parent

        if r1 != r2:                   # If the Parents Are Not Same
            self.parents[r2] = r1      # The create Parent of r2 to r1
            self.weight += w           # Incresing the Weight
            self.edgeCount += 1        # Increasing The EsgeCount by 1

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Step 1: Sorting the edges List
        edges = [(w,a,b,i) for i, (a,b,w) in enumerate(edges)]  # As we have to return i (index)
        edges.sort()

        # Step 2: Finding the First MinWeight In entire edges
        uf1 = UnionFind(n)
        for w, a, b, _ in edges:
            uf1.union(a, b, w)

        minWeight = uf1.weight

        # Step 3: Defining The Critical and Pseudo Critical Edges Empty 
        ce = []
        pce = []
        m = len(edges)


        # step 4: Now Including And Excludeing the edges to find Critical and PsuedoCritical edges
        for i in range(m):
            uf2 = UnionFind(n)              # Creting New uf2 UnionFind Class
            for j in range(m):              # for every edge
                if i == j:
                    continue
                w,a,b,_ = edges[j]    
                uf2.union(a,b,w)            # Unioning the x, y
            
            # if curr weight is greather or we didn't draw the proper graph
            if uf2.weight > minWeight or uf2.edgeCount < n-1:
                ce.append(edges[i][3])     # It is a Critical Edge


            else:
                # Forcefully adding the edge i and again doing MST Algo
                uf3 = UnionFind(n)               # creating new object Class
                w,a,b,_ = edges[i]               # taking the i edges
                uf3.union(a,b,w)                 # unioning the first i edge
                for j in range(m):
                    w,a,b,_ = edges[j]           # Uninoning the edges acordingly
                    uf3.union(a,b,w)
                
                if uf3.weight == minWeight:      # If curr weight == min wight
                    pce.append(edges[i][3])      # it is a PseudoCritical Edge

        return ce, pce    # Now Returning The Critical Edge And PseudoCretical Edge