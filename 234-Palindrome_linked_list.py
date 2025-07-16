# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Fast slow pointers to find middle
        slow = fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half of list
        current = middle = slow
        prev = None
        while(current):
            nextNode = current.next
            current.next = prev

            # Move forward
            prev = current
            current = nextNode

        # Compare first half with second half
        l, r = head, prev
        while(r):
            if(l.val != r.val):
                return False
            l = l.next
            r = r.next
        return True
