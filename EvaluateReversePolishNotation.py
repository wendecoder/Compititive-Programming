class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        length = len(tokens)
        stack = []
        for i in range(length):
            if tokens[i] == '*':
                s = len(stack)
                newt = stack[s-2] * stack[s-1]
                for i in range(2):
                    stack.pop()
                stack.append(newt)
            elif tokens[i] == '/':
                s = len(stack)
                newt = stack[s-2] / stack[s-1]
                newt = int(newt)
                for i in range(2):
                    stack.pop()
                stack.append(newt)
            elif tokens[i] == '+':
                s = len(stack)
                newt = stack[s-2] + stack[s-1]
                for i in range(2):
                    stack.pop()
                stack.append(newt)
            elif tokens[i] == '-':
                s = len(stack)
                newt = stack[s-2] - stack[s-1]
                for i in range(2):
                    stack.pop()
                stack.append(newt)
            else:
                stack.append(int(tokens[i]))
        return stack[0]
                
                
