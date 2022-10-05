class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                continue 
            elif nums[i]==nums[i-1]:
                ans+=1
                nums[i]=nums[i]+1
            else:
                s=nums[i-1]-nums[i]+1
                ans+=s
                nums[i]=nums[i]+s
            print(nums[i])
        return ans
            
                
            
        return 0