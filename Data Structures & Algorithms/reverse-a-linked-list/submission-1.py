# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prevhead = None
        while head:
            nexthead = head.next
            head.next = prevhead
            prevhead = head
            head = nexthead
        # head.next = prevhead
        return prevhead
        

            