class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        s=0
        nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                if abs(nums[i]-nums[j])==k:
                    s+=1
                    
        return s