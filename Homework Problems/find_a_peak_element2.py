from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            max_row = 0
            for i in range(m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
            
            left_is_bigger = mid - 1 >= 0 and mat[max_row][mid - 1] > mat[max_row][mid]
            right_is_bigger = mid + 1 < n and mat[max_row][mid + 1] > mat[max_row][mid]
            
            if not left_is_bigger and not right_is_bigger:
                return [max_row, mid]
            elif right_is_bigger:
                left = mid + 1
            else:
                right = mid - 1
        
        return [-1, -1]