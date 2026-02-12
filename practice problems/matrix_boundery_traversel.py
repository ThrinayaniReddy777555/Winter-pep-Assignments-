
        # code here 
from typing import List

class Solution:
    def boundaryTraversal(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        n, m = len(matrix), len(matrix[0])
        top, bottom = 0, n - 1
        left, right = 0, m - 1

        res = []

        for j in range(left, right + 1):
            res.append(matrix[top][j])

        for i in range(top + 1, bottom + 1):
            res.append(matrix[i][right])

        if top != bottom:
            for j in range(right - 1, left - 1, -1):
                res.append(matrix[bottom][j])

        if left != right:
            for i in range(bottom - 1, top, -1):
                res.append(matrix[i][left])

        return res
