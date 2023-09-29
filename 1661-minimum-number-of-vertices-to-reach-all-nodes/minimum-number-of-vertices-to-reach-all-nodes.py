class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable = [0] * n

        for i, (f, t) in enumerate(edges):
            # if not reachable, then it has to be a source
            reachable[t] += 1

        # if reachable[i] == 0, then this node would have to be included in the output

        output = []

        for i in range(n):
            if reachable[i] == 0:
                output.append(i)
        return output
