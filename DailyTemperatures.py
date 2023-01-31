class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] * len(temperatures)
        stack1 = []
        for i in range(len(temperatures)):
            while stack1 and temperatures[i] > temperatures[stack1[-1]]:
                index = stack1.pop()
                stack[index] = i - index
            stack1.append(i)
        return stack



        # stack = [0] * len(temperatures)
        # for j in range(len(temperatures) - 1):
        #     stack1 = []
        #     k = j + 1
        #     if temperatures[j] < temperatures[k]:
        #         stack[j] = 1
        #     else:
        #         if temperatures[k] == temperatures[len(temperatures) - 1]:
        #             stack[j] = 0
        #         else:
        #             while temperatures[j] > temperatures[k] and k <=len(temperatures) - 1:
        #                 if temperatures[j] == temperatures[len(temperatures) - 2]:
        #                     stack[j] = 0
        #                     break
        #                 else:
        #                     stack1.append(temperatures[j])
        #                     k = k + 1
        #             stack[j] = len(stack1) + 1
        # return stack
