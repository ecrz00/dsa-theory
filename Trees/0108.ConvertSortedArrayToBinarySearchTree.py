'''
Approach: 
We will use Binary Search to get the value at the middle-th index, every time a new node is created. For sake of simplicity, see the diagram bellow:

              8
            /    \ 
          /        \
        /            \ 
      4                12
    /   \           /       \
  2       6       10          14
/   \   /   \   /    \      /    \
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Every middle element became a node, and the new low and high limits became the left and right subtree.
Complexity:
- Time: O(n) -> Each element in the array is visited once to create a node.
- Space: O(log n) -> The depth of the recursion stack for a balanced tree.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def sortedArrayToBST(nums: list[int]) -> TreeNode:
    if not nums: return None
    def buildTree(lo, hi):
        if lo>hi: return None
        mid = lo + (hi-lo)//2
        root = TreeNode(nums[mid])
        root.left = buildTree(lo, mid-1)
        root.right = buildTree(mid+1, hi)
        return root
    return buildTree(0, len(nums)-1)