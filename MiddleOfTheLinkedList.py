# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        curr1 = head
        numOfElem = 0
        x = 1
        while curr:
            curr = curr.next
            numOfElem = numOfElem + 1
        if numOfElem / 2 < (numOfElem // 2) + 1:
            while x < numOfElem // 2 + 1:
                curr1 = curr1.next
                x = x + 1
        else:
            while x <= numOfElem // 2 + 1:
                curr1 = curr1.next
                x = x + 1
        return curr1
