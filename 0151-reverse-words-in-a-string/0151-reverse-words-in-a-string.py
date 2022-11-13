class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        s=s[::-1]
        res=""
   
        for char in s:
            if char!="":
                res+=char
                res+=" "
            
          
            
    
        return res[:-1]
        