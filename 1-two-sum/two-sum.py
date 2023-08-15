class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # vanilla version
    #    for i in range(len(nums)):
    #        for j in range(len(nums)):
    #            if nums[i] + nums[j] == target and i != j:
    #                return [i, j]

    # faster version

        values = []

        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in values:
                return [i, values.index(residual)]
            else:
                values.append(nums[i])

