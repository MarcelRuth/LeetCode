class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        num_dic = {
            'number' : [],
            'counts' : []
        }

        for i in range(len(nums)):
            if nums[i] not in num_dic['number']:
                num_dic['number'].append(nums[i])
                num_dic['counts'].append(1)
            else:
                index = num_dic['number'].index(nums[i])
                num_dic['counts'][index] += 1

        num_counts, num_list =[list(x) for x in zip(*sorted(zip(num_dic['counts'], num_dic['number']), key=lambda pair: pair[0] ))]
        
        return num_list[-1]