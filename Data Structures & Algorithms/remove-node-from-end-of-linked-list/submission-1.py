# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        curr = head
        while curr.next: 
            length += 1
            curr = curr.next

        if length == 1 and n == 1: 
            return None

        remove = length - n + 1
        count = 1
        curr, prev = head, None
        if remove == 1: 
            return head.next
        while count != remove: 
            count += 1
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head

        