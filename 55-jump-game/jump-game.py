class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # jump_range = nums[0]
        # while len(nums) > 1 and jump_range != 0 and nums[0] < len(nums) - 1:
        #     jump_range = nums[0]
        #     # exclude first element becauses that is where we are currently
        #     # we can reach index + 1
        #     next_jumps = [x+i if x != 0 else 0 for i, x in enumerate(nums[ 1 : jump_range + 1])] 
        #     max_jump_range = max(next_jumps)
        #     max_jump_index = next_jumps.index(max_jump_range)
        #     if max_jump_range == 0:
        #         return False
        #     nums[:] = nums[max_jump_index + 1 : ]

        # if nums[0] >= len(nums) - 1:
        #     return True
        # else:
        #     return False
        
        # back iteration approach

        goal = len(nums) - 1 # last index
        # goal has to appraoch zero

        # iterate from the back
        # reverse range from len(nums) - 2 
        # -1 from index starting from 0
        # -1 from starting next to last index
        for i in range(len(nums)-2, -1, -1):
            if goal == 0:
                return True
            # going back the index and checking if goal can be reached
            if i + nums[i] >= goal:
                # now we can reach goal and update the node that we can reach the goal from
                goal = i
        # did not converge
        if goal != 0:
            return False
        else:
            return True
    
        
