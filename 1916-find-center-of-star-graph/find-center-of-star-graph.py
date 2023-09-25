class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        # the node has to be in every entry of the edge indices
        # as there are n - 1 edges, no node has more than 1 edge, except 
        # the center node, so the one that is in the first two entries is duplicate

        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]

        