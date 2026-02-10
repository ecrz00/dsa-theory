'''
Approach:
The solution implements a Floyd's Cycle-Finding algorithm, also known as 'fast and slow pointers'. If the list is linear, the fast pointer will reach the end; however, if there is a cycle, the fast pointer will eventually catch up to the slow one from behind.

Complexity:
- Time: O(n) -> In the worst case, fast travels twice the distance of slow.
- Space: O(1) -> We only use two pointer variables.
'''
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False