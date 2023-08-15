# no sorting
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:                
        # find middle
        pivot = nums[len(nums)//2]

        left = [x for x in nums if x < pivot]
        # smaller than mid
        mid  = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        # greater than mid

        L = len(left)
        R = len(right)
        M = len(mid)

        if k > R + M: # k is greater than the large values and the mid
            # search in the left part and M and R should be substracted from k
            return self.findKthLargest(left, k-R-M)
        elif k <= R: # the element is in the large part already
            return self.findKthLargest(right, k)
        else:
            # it is in the middle
            return mid[0]
