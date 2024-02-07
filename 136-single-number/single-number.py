class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        the_one = set()

        for i in range(len(nums)):
            # second occurance removes nums
            if nums[i] in the_one:
                the_one.remove(nums[i])
                continue
            # first occurance adds
            the_one.add(nums[i])
        
        # went through the whole list
        # only left is 'the one'

        return the_one.pop()