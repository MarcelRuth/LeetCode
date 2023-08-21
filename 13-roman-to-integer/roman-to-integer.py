class Solution:
    def romanToInt(self, s: str) -> int:
        
        convert_dic = {
            "I"         :       1,
            "V"         :       5,
            "X"         :       10,
            "L"         :       50,
            "C"         :      100,
            "D"         :      500,
            "M"         :     1000,
        }

        int_sum = 0
        was_used = False # checks if symbol was already used 
    
        for i, symbol in enumerate(s):
            current_value = convert_dic[symbol]
            if not was_used and i != len(s) - 1:
                # check if next value is lower or equal
                # lower or equal values can only be added
                if convert_dic[s[i+1]] <= current_value:
                    # its smaller hence current value can be used
                    int_sum += current_value
                    was_used = False

                # check if next is larger
                # meaning the current one is substracted from the next one
                elif convert_dic[s[i+1]] > current_value:
                    current_value = convert_dic[s[i+1]] - current_value
                    int_sum += current_value

                    # ignore next symbol
                    was_used = True

            elif i == len(s) - 1 and not was_used:
                int_sum += current_value
            else:
                was_used = False

        return int_sum