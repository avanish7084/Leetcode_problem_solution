# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        def order(queue):
            if root is None:
                return res
            if len(queue)==0:
                return 
            k=[]
            for i in queue:
                k.append(i.val)
            res.append(sum(k)/len(k))
            temp=[]
            for i in queue:
                if i.left!=None:
                    temp.append(i.left)
                if i.right!=None:
                    temp.append(i.right)
            order(temp)
        
        order([root])
        return res
        