class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]
            
        if "" in strs:
            return ""

        len_0 = len(strs[0])
        counter = 0

        for i in range(1, len_0+1):
            prefix =  strs[0][:i]
            for word in strs:
                if prefix in word[:i]:
                    continue
                else:
                    # if this happens, then its over already
                    if counter == 0:
                        return ""
                    else:
                        print('here')
                        return strs[0][:counter]
            counter += 1

        # if it never happened
        return strs[0][:counter+1]