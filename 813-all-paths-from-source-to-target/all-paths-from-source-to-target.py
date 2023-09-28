class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:       
        q =[[0]]
        target= len(graph) -1 
        res = []        
        while q:
            curr_node = q.pop(0)
            if curr_node[-1] == target:
                res.append(curr_node)            
            for neighbor in graph[curr_node[-1]]:
                q.append(curr_node + [neighbor])       
        return res
