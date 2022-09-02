"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        if root is None:
            return
        def level_ord(queue):
            if len(queue)==0:
                return
            temp=[]
            for i in queue:
                temp.append(i.val)
            res.append(temp)
            k=[]
            for i in queue:
                k.extend(i.children)
            level_ord(k)
        level_ord([root])
        return res