'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def differenceSum(self, root1, root2):
        # write your code here
        def helper(n1, n2):
            if not n1 and not n2:
                return 0

            val1 = n1.data if n1 else 0
            val2 = n2.data if n2 else 0

            diff = abs(val1 - val2)

            left_diff = helper(n1.left if n1 else None, n2.left if n2 else None)
            right_diff = helper(n1.right if n1 else None, n2.right if n2 else None)

            return diff + left_diff + right_diff

        return helper(root1, root2)