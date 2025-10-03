# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Reverse second half, merge with first half
        # Find second half
        fast = head
        slow = fast
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        # Reverse second half (starts from slow pointer)
        prev = None
        current = slow.next
        slow.next = None # Disconnect the two halves before reversing
        while(current):
            nextNode = current.next
            current.next = prev
            # move both pointers forward
            prev = current
            current = nextNode
        # Merge the two halves
        l1 = head
        l2 = prev
        while(l2):
            l1Next = l1.next
            l2Next = l2.next
            # Pointers change
            l1.next = l2
            l2.next = l1Next
            # Move pointers forward
            l1 = l1Next
            l2 = l2Next

