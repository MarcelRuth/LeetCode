class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        large = len(numbers) - 1
        small = 0

        while small != large:
            if numbers[small] + numbers[large] == target:
                return [small + 1, large + 1] # one indexed
            elif numbers[small] + numbers[large] > target:
                large -= 1
            else:
                small += 1
        
