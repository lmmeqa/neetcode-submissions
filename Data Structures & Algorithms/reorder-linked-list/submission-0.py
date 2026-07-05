# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        array = []
        while head:
            array.append(head)
            head = head.next
        left,right = 0, len(array) - 1
        while left<right:
            print(left, right)
            array[left].next = array[right]
            if left+1 < right:
                array[right].next = array[left + 1]
            left+=1
            right-=1
        array[left].next = None

        

        