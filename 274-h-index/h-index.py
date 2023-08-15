class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hIndex_val = 0
        for i in range(1, max(citations) + 1):
            minHindex = [x for x in citations if x >= i]
            if len(minHindex) >= i:
                hIndex_val = i
        return hIndex_val
                