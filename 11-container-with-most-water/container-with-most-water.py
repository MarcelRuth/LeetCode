class Solution:
    def maxArea(self, height: List[int]) -> int:

        left_pointer = 0
        right_pointer = len(height) - 1
        max_water = 0 

        def calc_water(left, right):
            return (right - left) * min(height[right], height[left])

        while left_pointer != right_pointer:

            cur_water = calc_water(left_pointer, right_pointer)
            if cur_water > max_water:
                max_water = cur_water
            
            if height[left_pointer] <= height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water



        