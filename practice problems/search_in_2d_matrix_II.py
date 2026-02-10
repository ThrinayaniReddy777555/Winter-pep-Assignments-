class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m=len(matrix)
        n=len(matrix[0])
        row=0
        col=n-1
        while row<m and col >= 0:
            curr_val = matrix[row][col]
            if curr_val == target: 
                return True
            elif curr_val > target:
                col-=1
            else:
                row+=1
        return False 

        
        
