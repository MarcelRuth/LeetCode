class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        gasTank, totalGas, start = 0, 0, 0
        
        for i in range(n):
            diff = gas[i] - cost[i]
            gasTank += diff
            totalGas += diff
            # If gasTank is negative, we can't reach the next station from the current start
            if gasTank < 0:
                gasTank = 0
                start = i + 1  # Mark the next station as the potential starting point
        
        # If totalGas is non-negative, we have found a valid starting point
        return start if totalGas >= 0 else -1