'''
Approach:
We will traverse both trees at the same time using DFS and comparing nodes at each position.

Visual Trace:
Tree P:      1         Tree Q:      1
            / \                    / \
           2   3                  2   3
          /                      /
         4                      4


- Compare P(1) and Q(1): Match! -> Move to left.
- Compare P(2) and Q(2): Match! -> Move to left.
- Compare P(4) and Q(4): Match! -> Move to left.
- Compare P(None) and Q(None): Match! Return True and go back to node 4 -> Move to right.
- Compare P(None) and Q(None): Match! Return True and go back to node 2. 
- Both children matched! Return True  and go back to Root.
- Now move to Right children P(3) and Q(3)...

Complexity:
- Time: O(n) -> Worst case we traverse the whole tree
- Space: O(n) -> Recursion stack depth equals the height of the tree.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    def isSame(p,q):
        if not p and not q:
            return True
        if p and not q or q and not p:
            return False
        if p.val != q.val: 
            return False
        return isSame(p.left, q.left) and isSame(p.right, q.right)
    return isSame(p,q)