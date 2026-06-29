class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix:
            return res
           
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
       
        while left <= right and top <= bottom:
            # 1. Right ->
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
           
            # 2. Down V
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
           
            # 3. Left <- (Check if row still exists)
            if not (left <= right and top <= bottom):
                break
               
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
           
            # 4. Up ^ (Check if column still exists)
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
           
        return res


       
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
        left += 1
        return res


