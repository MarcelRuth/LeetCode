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

        counter = {key: value for key, value in sorted(counter.items(), key=lambda item: item[1], reverse=True)}
        for key in counter:
            for key2 in counter:
                if key != key2:
                    if [key, key2] in roads or [key2, key] in roads:
                        pot_max_rank = counter[key] + counter[key2] - 1
                    else:
                        pot_max_rank = counter[key] + counter[key2]
                    if pot_max_rank > max_rank:
                        max_rank = pot_max_rank

        return max_rank
