'''
You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.
    Example 1: 
        +---+    +---+    +---+
        | 1 | -> | 2 | -> | 4 |
        +---+    +---+    +---+
       
        +---+    +---+    +---+
        | 1 | -> | 3 | -> | 4 |
        +---+    +---+    +---+
       
        +---+    +---+    +---+    +---+    +---+    +---+
        | 1 | -> | 1 | -> | 2 | -> | 3 | -> | 4 | -> | 4 |
        +---+    +---+    +---+    +---+    +---+    +---+
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]

    Example 2:
        Input: list1 = [], list2 = []
        Output: []

    Example 3:
        Input: list1 = [], list2 = [0]
        Output: [0]
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode: #T: O(n) S: O(1)
    hd = ListNode()
    cur = hd
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1.val
            list1 = list1.next
        else:
            cur.next = list2.val
            list2 = list2.next
        cur = cur.next
    cur.next = list1 if list1 else list2
    return hd.next