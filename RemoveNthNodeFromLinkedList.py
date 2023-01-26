# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        curr1 = head 
        numNode = 0
        x = 1
        while curr:
            curr = curr.next
            numNode = numNode + 1
        nodtodel = numNode - n
        if numNode == 1 and nodtodel == 0:
            head = None
            return head
        elif nodtodel == 0:
            curr1 = curr1.next
            return curr1
        else:
            while x < nodtodel:
                curr1 = curr1.next
                x = x + 1
            if curr1.next.next:
                curr1.next = curr1.next.next
            else:
                curr1.next = None
            return head
