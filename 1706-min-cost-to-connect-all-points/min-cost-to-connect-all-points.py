from typing import List, Tuple
import heapq
from collections import defaultdict

def manhattan_distance(p1: List[int], p2: List[int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def update_heap_and_dict(heap: List[Tuple[int, int]], heap_dict: dict, new_distance: int, v: int):
    if new_distance < heap_dict[v]:
        heap_dict[v] = new_distance
        heapq.heappush(heap, (new_distance, v))

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        heap_dict = defaultdict(lambda: float('inf'))
        min_heap = [(0, 0)]
        
        mst_weight = 0
        
        while min_heap:
            w, u = heapq.heappop(min_heap)
            
            if visited[u] or heap_dict[u] < w:
                continue
            
            visited[u] = True
            mst_weight += w
            
            for v in range(n):
                if not visited[v]:
                    new_distance = manhattan_distance(points[u], points[v])
                    update_heap_and_dict(min_heap, heap_dict, new_distance, v)
        
        return mst_weight
