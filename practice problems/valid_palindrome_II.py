class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali(i, j):
            return all(s[k] == s[i + j - k]     
        for k in range(i, i + (j - i) // 2 + 1))

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_pali(left + 1, right) or is_pali(left, right - 1)
            left += 1
            right -= 1
        return True 
