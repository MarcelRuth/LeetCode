class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i, x in enumerate(nums):

            if target == x:
                return i
            
            if target < x:
                return i
                
        # if this is reached
        # target is larger than the largest x in nums

        return len(nums)