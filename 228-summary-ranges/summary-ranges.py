class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        curr_str = ''

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(n) for n in nums]

        for i, n in enumerate(nums):

            if i == 0:
                curr_str = str(n)
                if nums[i+1] != n + 1:
                    output.append(curr_str)
                    curr_str = ''
                continue
                
            if i != len(nums) - 1:
                if nums[i+1] == n + 1:
                    if len(curr_str) == 0:
                        curr_str = str(n)
                    continue

            # we have a start number 
            # cap sequence as this is the last
            # number that fits
            if len(curr_str) != 0:
                curr_str += '->' + str(n)
                output.append(curr_str)
                curr_str = ''
                continue

            # no start number but next 
            # number not in range
            curr_str = str(n)
            output.append(curr_str)
            curr_str = ''
            continue
            
        return output

        