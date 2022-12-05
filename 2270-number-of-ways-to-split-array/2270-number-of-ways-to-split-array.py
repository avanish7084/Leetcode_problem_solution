class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums)==1:
            return 0
        prefix_arry,post_arry=[],[]
        res=[]
        s,r=0,0
        for i in range(n-1):
            s+=nums[i]
            r+=nums[n-i-1]
            prefix_arry.append(s)
            post_arry.append(r)
            
        post_arry=post_arry[::-1]
        
        ans=0
        for i in range(n-1):
            if post_arry[i]<=prefix_arry[i]:
                ans+=1
        return ans
        print(prefix_arry,post_arry)
        
            
        
        
        