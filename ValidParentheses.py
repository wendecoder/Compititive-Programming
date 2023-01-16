class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        length = len(s)
        for x in s:
            if x in ['(', '{', '[']:
                stack.append(x)
            elif x == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif x == '}' and len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            elif x == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                return False
        return stack == []
