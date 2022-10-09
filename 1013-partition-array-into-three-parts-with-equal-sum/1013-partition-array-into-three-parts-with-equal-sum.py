class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
        
        """
        
        n=len(arr)
        i=0
        while i<n-2:
            s=sum(arr[:i+1])
            j=i+1
            while j<n-1:
                s1=sum(arr[i+1:j+1])
                if s==s1 and s1==sum(arr[j+1:]):
                    return True
                else:
                    j+=1
            i+=1
            
        return False
        
        """
        n=len(arr)
        i=0
        s=sum(arr)
        
        if s%3!=0:
            return False
        avg=s//3
        temp=0
        ans=0
        for i in range(n):
            temp+=arr[i]
            if temp==avg:
                temp=0
                ans+=1
        return ans>=3
            
        
        
        
        
        
        
            