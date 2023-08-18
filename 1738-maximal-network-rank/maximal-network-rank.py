class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        # it is a graph and we are looking for two connected nodes
        # that have the most edges attached to them
        counter = [0] * n
        max_rank = 0

        # used to check for connections later
        graph = [[False] * n for _ in range(n)]

        for edge in roads:
            # first count the edges of each node
            counter[edge[0]] += 1
            counter[edge[1]] += 1

            # set edges in the graph
            graph[edge[0]][edge[1]] = graph[edge[1]][edge[0]] = True


        # check all combinations
        for i in range(n):
            for j in range(i + 1, n):
                pot_max_rank = counter[i] + counter[j] 
                if graph[i][j]: # connected nodes
                    pot_max_rank -= 1
                max_rank = max(max_rank, pot_max_rank)

        return max_rank
