'''
Approach:
Iterative BFS using a queue to count how many levels we can fully traverse before the queue is empty.
          3         -> Level 1 (aux = [3])
         / \
        9   20      -> Level 2 (aux = [9,20])
            / \
           15  7    -> Level 3 (aux = [15,7])
At each level we will store the append the level-order values into res. Finally the array inverted is returned.

Complexity:
- Time: O(n) -> Visiting each node.
- Space: O(n) -> To store the result and the queue.
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def levelOrderBottom(root: TreeNode) -> list[list[int]]:
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
        return res[::-1]