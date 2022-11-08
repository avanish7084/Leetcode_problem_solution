class Solution:
    def makeGood(self, s: str) -> str:
        res=[]
        
        for i in range(len(s)):
            
            if len(res)!=0 and abs(ord(s[i])-ord(res[-1]))==32:
                res.pop()
            else:
                res.append(s[i])
            
        
        
        return "".join(res)
