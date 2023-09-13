# from collections import deque
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # deque approach
        # slow but low memory
        # q = deque([], k)
        # for n in nums:
        #     if n in q:
        #         return True
        #     q.append(n)
        # return False
        hs = {}
        for i, n in enumerate(nums):
            if n in hs and abs(i - hs[n]) <= k:
                return True
            hs[n] = i
        return False
