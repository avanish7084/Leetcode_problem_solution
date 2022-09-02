"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        def preorder(root):
            if root is None:
                return
            res.append(root.val)
            if root.children!=None:
                for i in root.children:
                    preorder(i)
        preorder(root)
        return res
            
                