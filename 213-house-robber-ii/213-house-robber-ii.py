class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)-1
        n1=len(nums)
        if n1==1:
            return nums[0]
        if n1==2:
            return max(nums[0],nums[1])
        def hose1(dp1,nums,i):
            
            if i==n1-1:
                dp1[i]=nums[i]
                return dp1[i]
            if i in dp1:
                return dp1[i]
            if i==n1:
                dp1[i]=0
            
            else:
                ans=max(nums[i]+hose1(dp1,nums,i+2),hose1(dp1,nums,i+1))
                dp1[i]=ans
            return dp1[i]
        def hose(dp1,nums,i):
            
            if i==n-1:
                dp1[i]=nums[i]
                return dp1[i]
            if i in dp1:
                return dp1[i]
            if i==n:
                dp1[i]=0
            
            else:
                ans=max(nums[i]+hose(dp1,nums,i+2),hose(dp1,nums,i+1))
                dp1[i]=ans
            return dp1[i]
        ans1=hose({},nums,0)
        ans2=hose1({},nums,1)
        return max(ans1,ans2)
                
    
            