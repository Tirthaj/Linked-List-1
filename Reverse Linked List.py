# Time : O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        curr = head
        prev = None
        fast = curr.next
        while fast:
            curr.next = prev
            prev = curr
            curr = fast
            fast = fast.next
        curr.next = prev

        return curr