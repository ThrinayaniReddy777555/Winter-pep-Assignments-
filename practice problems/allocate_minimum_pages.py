
class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        if k > n:
            return -1

        left = max(arr)    
        right = sum(arr)   
        ans = -1

        def canAllocate(maxPages):
            students = 1
            pages = 0

            for book in arr:
                if pages + book <= maxPages:
                    pages += book
                else:
                    students += 1
                    pages = book

                    if students > k:
                        return False

            return True

        while left <= right:
            mid = (left + right) // 2

            if canAllocate(mid):
                ans = mid
                right = mid - 1   
            else:
                left = mid + 1    

        return ans

