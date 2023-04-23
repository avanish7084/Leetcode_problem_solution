class Solution:
    def minimumSum(self, num: int) -> int:
        l=list(str(num))
        l.sort()
        l1=l[0]+l[3]
        l2=l[1]+l[2]
        res=int(l1)+int(l2)
        return res