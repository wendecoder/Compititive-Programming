class Solution:
    def reverseParentheses(self, s: str) -> str:
        length = len(s)
        stack = []
        for i in range(length):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                temp = s[stack[-1]:i + 1]
                s = s[:stack[-1]] + temp[::-1] + s[i + 1:]
                stack.pop()
        ans = ""
        for i in range(length):
            if s[i] not in '()':
                ans = ans + (s[i])
        return ans




                
            
