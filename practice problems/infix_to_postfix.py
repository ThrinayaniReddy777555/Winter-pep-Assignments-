class Solution:
    def infixtoPostfix(self, a):
        #code here
        ans = ""
        stack = []
        for s in a:
            if s not in "^/+-*()":
                ans += s
                continue
            if not stack:
                stack.append(s)
                continue
            if s == ")":
                while stack and stack[-1] != "(":
                    ans += stack.pop()
                if stack: stack.pop()
            elif s in "+-":
                while stack and stack[-1] in "+-*/^":
                    ans += stack.pop()
            elif s in "/*":
                while stack and stack[-1] in "^/*":
                    ans += stack.pop()
            if s != ")":
                stack.append(s) 
        while stack:
            ans += stack.pop()
        
        return ans
        #code here
        
        