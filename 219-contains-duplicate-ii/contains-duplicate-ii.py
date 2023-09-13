from collections import deque
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        q = deque([], k)
        for n in nums:
            if n in q:
                return True
            q.append(n)
        return False
