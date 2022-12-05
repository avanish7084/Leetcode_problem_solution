class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        n=len(nums)
        if len(nums)==1:
            return 0
        prefix_arry,post_arry=[],[]
        res=[]
        s,r=0,0
        for i in range(n):
            s+=nums[i]
            r+=nums[n-i-1]
            prefix_arry.append(s//(i+1))
            post_arry.append(r//(i+1))
            
        post_arry=post_arry[:n-1]
        post_arry=post_arry[::-1]
        post_arry.append(0)
        
        ans=-1
        an=1000000
        for i in range(n):
            s=abs(prefix_arry[i]-post_arry[i])
            if an>s:
                an=s
                ans=i
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         an=1000000
#         # print(type(an))
#         ans=-1
#         if len(nums)==1:
#             return 0
#         prefix_arry,post_arry=[],[]
        
#         for i in range(len(nums)):
#             if (i+1)<len(nums):
#                 l=nums[:i+1]
#                 left_avg=sum(l)//len(l)
#                 r=nums[i+1:]
#                 right_avg=sum(r)//len(r)
                
#                 s=abs(left_avg-right_avg)
                
#                 if an>s:
                   
#                     an=s
#                     ans=i
#         return ans