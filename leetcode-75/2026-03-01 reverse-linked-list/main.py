# Approach: Iterate through the list while reversing pointers using prev and curr references.
# Time Complexity: O(n), each node is visited once.
# Space Complexity: O(1), in-place pointer reversal.
# Edge Cases: empty list, single node, two nodes.
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        prev = None
        curr = head
        while curr is not None:
            nNode = curr.next
            curr.next = prev
            prev = curr
            curr = nNode
        return prev
