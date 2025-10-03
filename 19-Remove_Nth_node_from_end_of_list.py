# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        front = dummy
        back = dummy
        # move front pointer to nth node
        for _ in range(n):
            front = front.next
        # Move pointers simultaneously until reached end of list
        while(front.next):
            front = front.next
            back = back.next
        # back is now one node before target node to delete
        back.next = back.next.next
        return dummy.next
