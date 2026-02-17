import bisect
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        l = bisect.bisect_right(letters, target)
        return letters[l % len(letters)]

