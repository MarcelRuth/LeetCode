
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        distance = 0
        for i in range(1, len(prices)):
            if prices[i] > min_:
                if prices[i] - min_ > distance:
                    distance = prices[i] - min_
            else:
                min_ = prices[i]

        return distance


