# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.res=""
        if root is None:
            return ""
        
        def traverse(root):
            
            if root is None:
                return
            self.res+=str(root.val)
            
            if root.left:
                self.res+="("
                traverse(root.left)
                self.res+=")"
            if not root.left and root.right:
                self.res+="()"
            if root.right:
                self.res+="("
                traverse(root.right)
                self.res+=")"
            return self.res
        return traverse(root)
        