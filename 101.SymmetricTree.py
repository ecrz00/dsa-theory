'''
A tree is symmetric if the left subtree is a mirror reflection of the right subtree.

Visual Trace:
      1
    /   \
   2     2
  / \   / \
 3   4 4   3

Recursive Comparison:
1. isSym(Root.left, Root.right) -> Compares node (2) and node (2).
2. To be symmetric, we cross-compare:
   a) Left of (2) with Right of (2) -> isSym(3, 3)  
   b) Right of (2) with Left of (2) -> isSym(4, 4) 

Complexity:
- Time: O(n) -> We visit every node once.
- Space: O(h) -> Height of the tree (recursion stack).
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isSymmetric(root: TreeNode) -> bool:
    def isSym(p,q):
        if not q and not p:
            return True
        if q and not p or p and not q:
            return False
        if q.val != p.val:
            return False
        return isSym(p.left, q.right) and isSym(p.right, q.left)
    return isSym(root, root)