# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ## Recursion
    ## Time complexity: O(n) since we visit each node exactly once.
    ## Space complexity: O(n) since we keep up to the entire tree. (worst case)
    #def validST(self, Node: TreeNode, Up: int, Low: int) -> bool:
    #    if Node is None:
    #        return True
    #    if Node.val >= Up or Node.val <= Low:
    #        return False
    #    Left = self.validST(Node.left, Node.val, Low)
    #    Right = self.validST(Node.right, Up, Node.val)
    #    return Left and Right
    #def isValidBST(self, root: TreeNode) -> bool:
    #    return self.validST(root, float('inf'), float('-inf'))
    
    ## Iteration
    ## Time complexity: O(n) since we visit each node exactly once.
    ## Space complexity: O(n) since we keep up to the entire tree. (worst case)
    #def isValidBST(self, root: TreeNode) -> bool:
    #    if not root:
    #        return True
    #    stack = [(root, float('-inf'), float('inf')),]
    #    while stack:
    #        root, lower, upper = stack.pop()
    #        if not root:
    #            continue
    #        if root.val <= lower or root.val >= upper:
    #            return False
    #        stack.append((root.right, root.val, upper))
    #        stack.append((root.left, lower, root.val))
    #    return True
    
    ## In-order traversal
    ## Time complexity: O(n) in the worst case when the tree is BST or the "bad" element is a rightmost leaf.
    ## Space complexity: O(n) to keep 'stack' functions (worst case).
    def __init__(self):
        self.last = float('-inf')
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        if not self.isValidBST(root.left): return False
        if self.last > float('-inf') and root.val <= self.last:
            return False
        self.last = root.val
        return self.isValidBST(root.right)
                    
