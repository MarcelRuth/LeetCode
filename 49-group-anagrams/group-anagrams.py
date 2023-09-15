class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        counters = {}

        for s in strs:
            counter_tuple = tuple(sorted(Counter(s).items()))
            if counter_tuple in counters:
                counters[counter_tuple].append(s)
            else:
                counters[counter_tuple] = [s]
        
        for key in counters:
            final_list.append(counters[key])
        
        return final_list