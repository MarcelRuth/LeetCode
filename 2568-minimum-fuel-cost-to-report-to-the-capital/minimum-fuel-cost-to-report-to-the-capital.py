class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        adj_m = defaultdict(list)

        for a, b in roads:
            adj_m[a].append(b)
            adj_m[b].append(a)

        ans = [0]

        def dfs(node, prev):
            people = 1

            # go through the neighbors
            for i in adj_m[node]:
                # don't visit same node twice
                if i == prev:
                    continue 
                
                # gather people
                people += dfs(i, node)

            # if we are not at the captial
            if node != 0:
                ans[0] += ceil(people/seats)
            
            return people

        # start dfs at node 0
        # no previous node
        dfs(0, None)

        return ans[0]
