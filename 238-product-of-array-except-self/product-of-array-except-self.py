class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        max_val = 1
        zero_counter = 0
        for i, x in enumerate(nums):
            if zero_counter <= 1:
                if x == 0:
                    zero_counter += 1
                    zero_index = i
                else:
                    max_val *= x
        if zero_counter == 1:
            answer = [0] * len(nums)
            answer[zero_index] = max_val
        elif zero_counter == 2:
            answer = [0] * len(nums)
        else:
            answer = [int(max_val * x**(-1)) for x in nums]
        return answer