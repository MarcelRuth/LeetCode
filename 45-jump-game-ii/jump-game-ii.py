class Solution:
    def jump(self, nums: List[int]) -> int:
        # starting from the back again and searching
        # for the best jump at the current position
        goal = len(nums) - 1
        num_jumps = 0
        while goal != 0:
            # search largest jumps first
            for i in range(1000, 0, -1): # possible jump ranges
                # val relative to goal in i
                if i <= goal:
                    if nums[goal - i] >= i: 
                        goal += - i
                        num_jumps += 1
                        break
        return num_jumps


