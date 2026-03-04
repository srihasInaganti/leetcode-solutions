from __future__ import annotations
from typing import Optional

# Approach: Use slow/fast pointers to find middle node. 
# Keep track of previous node and remove middle by skipping it.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Edge Cases: single node, two nodes

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        prev = None

        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head
