class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {}
        for i, char in enumerate(s):
            last_occ[char] = i
        
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            if char in seen:
                continue
            while stack and stack[-1] > char and last_occ[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
