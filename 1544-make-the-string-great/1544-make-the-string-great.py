class Solution:
    def makeGood(self, s: str) -> str:
        i=0
        while len(s)>1 and i<len(s)-1:
            if abs(ord(s[i])-ord(s[i+1]))==32:
                s=s[:i]+s[i+2:]
                return self.makeGood(s)
            
            i+=1
        return s
        
        
        
        
        
        
        
#         res=[]
        
#         for i in range(len(s)):
            
#             if len(res)!=0 and abs(ord(s[i])-ord(res[-1]))==32:
#                 res.pop()
#             else:
#                 res.append(s[i])
            
        
        
#         return "".join(res)
