class Solution:
    def intToRoman(self, num: int) -> str:
        convert_dic = {
            'I'     :       1,
            'V'     :       5,
            'X'     :       10,
            'L'     :       50,
            'C'     :       100,
            'D'     :       500,
            'M'     :       1000
        }

        roman_string = ''
        for i, key in enumerate(reversed(convert_dic)):
            while num >= convert_dic[key]:
                roman_string += key 
                num -= convert_dic[key]

            # start with the largest substraction
            for j, next_key in enumerate(reversed(convert_dic)):
                
                # also check that the combined values are not the same as the next one
                if j > i and num >= convert_dic[key] - convert_dic[next_key] and convert_dic[key] - convert_dic[next_key] != convert_dic[next_key]:
                    roman_string += next_key
                    roman_string += key
                    num -= convert_dic[key] - convert_dic[next_key]

        return roman_string


