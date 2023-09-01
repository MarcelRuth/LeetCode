class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == len(s):
            return s
        # add lists to this list
        # ending up with a matrix and lists as columns

        string_matrix = []
        left_counter = 0
        right_counter = numRows
        num_columns = 0
        while left_counter < len(s):
            i = num_columns
            # full column
            if left_counter >= len(s):
                left_counter = -1

            if i % (numRows - 1) == 0:
                string_matrix.append([s[left_counter:right_counter]])
                left_counter += numRows
                right_counter += numRows

            # diagonal
            else:
                filler_string_up = '$' * (1 + numRows - 2 - (i % (numRows - 1))) 
                filler_string_low = '$' * ((numRows) - len(filler_string_up) - 1)
                string_matrix.append([f'{filler_string_up}{s[left_counter]}{filler_string_low}'])
                left_counter += 1
                right_counter += 1

            num_columns += 1
        print(string_matrix)

        final_string = ''
        for i in range(numRows):
            for j in range(num_columns):
                # if last column, fill with $
                if j == num_columns - 1:
                    filler = '$' * (numRows - len(string_matrix[j]))
                    string_matrix[j][0] += filler
                final_string += string_matrix[j][0][i]

        return final_string.replace('$', '')

