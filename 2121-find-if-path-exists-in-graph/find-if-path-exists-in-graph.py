from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        # Create adjacency list representation of the graph
        graph = {i: [] for i in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        already_visited = set()

        # Edge cases
        if source == destination:
            return True

        if destination >= n or source >= n:
            return False

        # Recursive DFS function
        def explore(current_node, destination):
            if current_node == destination:
                return True

            already_visited.add(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in already_visited:
                    if explore(neighbor, destination):
                        return True

            return False

        return explore(source, destination)
