# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        self.ans = 0

        def f(node):
            if not node:
                return -float('inf')

            left = f(node.left)
            right = f(node.right)

            mx = max(left, right, node.val)

            if node.val == mx:
                self.ans += 1

            return mx

        f(root)
        return self.ans