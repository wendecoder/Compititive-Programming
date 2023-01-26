# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        stack = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        answer = [0] * len(values)
        i = 0
        for value in values:
            print(value)
            print(i)
            while stack and value > values[stack[-1]]:
                nexgret = stack.pop()
                answer[nexgret] = values[i]
            stack.append(i)
            i = i + 1
        return answer
        #     toggle = True
        #     for j in range(1 + i, n):
        #         if stack[i] < stack[j]:
        #             stack1.append(stack[j])
        #             toggle = False
        #             break
        #     if toggle:
        #         stack1.append(0)
        # return stack1

                
