# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Empty
        if(not head):
            return
        prev = None
        current = head
        while current:
            # Right pointer
            nextNode = current.next
            
            # Update link to point back
            current.next = prev

            # Move both forward
            prev = current
            current = nextNode
        return prev
            

