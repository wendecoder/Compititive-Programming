# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newlist = []
        curr = head
        while curr:
            newlist.append(curr.val)
            curr = curr.next
        newlist = sorted(newlist)
        curr2 = head
        i = 0
        while curr2:
            curr2.val = newlist[i]
            curr2 = curr2.next
            i = i + 1
        return head
