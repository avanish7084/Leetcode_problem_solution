class Solution:
    def compress(self, chars: List[str]) -> int:
        a=""
        c=1
        for i in range(len(chars)):
            if i==len(chars)-1 or chars[i]!=chars[i+1]:
                if c==1:
                    a+=chars[i]
                else:
                    a+=chars[i]+str(c)
                c=1
            
            else:
                c+=1
        n=len(a)
        for i in range(len(a)):
            chars[i]=a[i]
    
      
        return len(chars[:n])
                 
                