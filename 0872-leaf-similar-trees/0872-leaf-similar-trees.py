# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf=[]
    
        
        def traverse(root):
            if root is None:
                return 
            traverse(root.left)
            if root.left==None and root.right==None:
                leaf.append(root.val)
            traverse(root.right)
            
        traverse(root1)
        traverse(root2)
        print(leaf)
        n=len(leaf)
        h=n//2
        if n%2==0:
            for node in range(len(leaf)//2):
                if leaf[node]==leaf[node+h]:
                    continue 
                else:
                    return False
            return True
        else:
            return False
        
                    
                
        