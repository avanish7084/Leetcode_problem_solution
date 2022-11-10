class Solution:
    def removeDuplicates(self, s: str) -> str:
        # method 1
        """
        s=list(s)
        n=len(s)
        for i in range(n-1):
            if s[i]==s[i+1]:
                s=s[:i]+s[i+2:]
                return self.removeDuplicates(s)
        return "".join(s)
                
        """
        
        # method 2
        
        s=list(s)
        n=len(s)
        stack=[]
        for i in range(n):
            if stack and s[i]==stack[-1]:
                stack.pop()

            else:
                stack.append(s[i])
        return "".join(stack)