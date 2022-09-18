# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        res=[]
        def preorder(root):
            if root is None:
                return
            
            preorder(root.left)
            res.append(root.val)
            preorder(root.right)
        preorder(root)
        ans=float('inf')-res[0]
        for i in range(1,len(res)):
            m=abs(res[i]-res[i-1])
            if ans>m:
                ans=m
        return ans
                 
    
                
            