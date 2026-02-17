class Solution:
    def guessNumber(self, n: int) -> int:
        first = 1
        last = n
        while first<= last:
            mid = (first+last)//2
            ans = guess(mid) # type: ignore
            if ans == 0: 
                return mid
            else:
                if ans == -1:
                    last = mid-1
                    first = mid +1
        return -1
