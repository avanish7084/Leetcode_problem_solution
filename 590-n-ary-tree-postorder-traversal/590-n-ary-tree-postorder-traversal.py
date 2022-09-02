"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def postorder(root):
            if root is None:
                return
            for i in root.children:
                    postorder(i)
            # if root.children!=None:
            #     for i in root.children:
            #         postorder(i)
            res.append(root.val)
        postorder(root)
        return res