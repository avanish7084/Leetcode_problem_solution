class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # for i in range(n):
        #     if nums[i]!=(i+1) and nums[i-1]!=i-1:
        #         return [nums[i],nums[i]-1]
        # for i in range(n):
        #     if nums[i]!=(i+1):
        #         return [nums[i],nums[i]+1]
    
        Sum=sum(nums)
        s=list(set(nums))
        a=Sum-sum(s)
        d=n*(n+1)//2-sum(s)
        return [a,d]
                     
        h={}
        for i in range(n):
            if nums[i] in h:
                h[nums[i]]+=1
            else:
                h[nums[i]]=1
        print(h)
        for i in h:
            if h[i]>1:
                k=i
                break
        for i in range(1,n+1):
            if i not in nums:
                l=i
                break
                
        print(k,l)
        return [k,l]
    
    
    
    
     
       
        
    

            
            