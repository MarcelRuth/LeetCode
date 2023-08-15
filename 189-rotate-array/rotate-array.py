class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k < len(nums) and k != 0:
            nums[:] = nums[-k:] + nums[:]
            nums[:] = nums[:-k]         
        else:
            for i in range(k):
                nums[:] = nums[-1:] + nums[:]
                nums[:] = nums[:-1]