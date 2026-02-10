class Solution:
    def boundaryTraversal(self, mat):
        arr = []
        n = len(mat)        
        m = len(mat[0])     
        for j in range(n):
            arr.append(mat[0][j])
        for i in range(1, m):
            arr.append(mat[i][m - 1])
        for j in range(m - 2, -1, -1):
            arr.append(mat[n - 1][j])
        for i in range(n - 2, 0, -1):
            arr.append(mat[i][0])
        return arr
