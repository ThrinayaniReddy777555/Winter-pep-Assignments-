# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
      
        ans = [[0] * n for _ in range(n)]
        count = 1
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:
            
            for i in range(left, right + 1):
                ans[top][i] = count
                count += 1
            top += 1

            
            for i in range(top, bottom + 1):
                ans[i][right] = count
                count += 1
            right -= 1

            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans[bottom][i] = count
                    count += 1
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans[i][left] = count
                    count += 1
                left += 1

        return ans


        