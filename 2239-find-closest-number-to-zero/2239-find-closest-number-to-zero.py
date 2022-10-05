class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        k=1000000
        ans=0
        for i in range(len(nums)):
            if k>=abs(nums[i]-0):
                k=abs(nums[i])
                ans=nums[i]
        return ans