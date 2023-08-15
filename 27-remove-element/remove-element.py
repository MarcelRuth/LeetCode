class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        init_length = len(nums)
        nums[:] = [i for i in nums if i != val]
        k = len(nums)
        
        return k