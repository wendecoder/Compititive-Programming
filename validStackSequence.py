class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        length = 2 * len(pushed)
        stack = []
        j = 0
        for i in range(length):
            if popped[j] in stack:
                if stack.pop() == popped[j]:
                    j = j + 1
                    pass
                else:
                    return False
            else:
                stack.append(pushed[0])
                pushed.pop(0)
        if stack == []:
            return True
        else:
            return False
