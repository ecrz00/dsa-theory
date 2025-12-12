'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
Example 1:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]
        [1] -> {2} -> [3] -> {4}
                    |
                    V
        {2} -> [1] -> {4} -> [3]
Example 2:
    Input: head = []
    Output: []

Example 3:
    Input: head = [1]
    Output: [1]

Example 4:
    Input: head = [1,2,3]
    Output: [2,1,3]
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def swapPairs(head: ListNode) -> ListNode:# T: O(n) S: O(1)
    if not head or not head.next:
        return head
    hd = ListNode(0,head)
    cur = hd
    slow, fast = head, head.next
    while fast:
        nxt = fast.next
        cur.next = fast
        slow.next = nxt
        fast.next = slow
        cur = slow
        slow = nxt
        fast = nxt.next if nxt else None
    return hd.next
        