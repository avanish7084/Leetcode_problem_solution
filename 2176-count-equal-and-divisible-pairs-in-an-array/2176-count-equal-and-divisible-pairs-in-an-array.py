class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n=len(nums)
        s=0
        # nums.sort()
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and (i*j)%k==0:
                    s+=1
                    
        return s