# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

# first solution using recursion
# time: O(n)
# space: O(n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorder(self,node,l):
#         if node.left:
#             self.inorder(node.left,l)
#         l.append(node.val)
#         if node.right:
#             self.inorder(node.right,l)
            
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         l = []
#         if root:
#             self.inorder(root,l)
#         return l

# second solution with iterative
# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        nStack = []
        curr = root
        while True:
            if curr:
                nStack.append(curr)
                curr = curr.left
            elif nStack:
                curr = nStack.pop()
                res.append(curr.val)
                curr = curr.right
            else:
                break
        return res

        