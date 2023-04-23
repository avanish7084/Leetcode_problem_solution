class Solution:
    def alternateDigitSum(self, n: int) -> int:
        l=list(str(n))
        res=0
        for i in range(len(l)):
            if i%2==0:
                res+=int(l[i])
            else:
                res-=int(l[i])
        return res