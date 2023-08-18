class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        # it is a graph and we are looking for two connected nodes
        # that have the most edges attached to them
        counter = {}
        max_rank = 0

        for i in range(n):
            counter[i] = 0

        for edge in roads:
            # first count the edges of each node
            counter[edge[0]] += 1
            counter[edge[1]] += 1

        # check all combinations
        for key in counter:
            for key2 in counter:
                if key != key2:
                    if [key, key2] in roads or [key2, key] in roads:
                        pot_max_rank = counter[key] + counter[key2] - 1
                    else:
                        pot_max_rank = counter[key] + counter[key2]
                    max_rank = max(max_rank, pot_max_rank)

        return max_rank
