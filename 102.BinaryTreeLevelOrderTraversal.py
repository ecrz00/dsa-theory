'''
Approach:
We will perfom a BFS using a Queue, this means processing the tree level by level. A 'deque' is used for efficient O(1) pops from the left.

Visual Trace:
      1
     / \
    2   3
   /     \
  4       5

Step-by-step Execution:
- With q = [1] and n = 1:
   - Pop 1 and add [2, 3] to q -> res = [[1]]
   -

-With q = [2, 3] and n = 2:
   - Pop 2 and add [4] to q.
   - Pop 3 and add children [5] to q -> res = [[1], [2, 3]]

- With q = [4, 5]. n = 2.
   - Pop 4.
   - Pop 5 -> res = [[1], [2, 3], [4, 5]]

Complexity:
- Time: O(n) -> Every node is visited and put into the queue once.
- Space: O(n)
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def levelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    q = deque()
    q.append(root)
    res = []
    while q:
        aux = []
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            aux.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(aux)
    return res