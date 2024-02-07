class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        rows = [[1], [1, 1]]
        for i in range(1, numRows - 1):
            row = [1]
            for j in range(len(rows[i]) - 1):
                row.append(rows[i][j] + rows[i][j+1])
            row.append(1)
            rows.append(row)
        return rows