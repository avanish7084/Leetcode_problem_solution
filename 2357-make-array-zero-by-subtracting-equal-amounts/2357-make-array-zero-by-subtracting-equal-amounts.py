class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)):
            if nums[i] not in res and nums[i]!=0:
                res.append(nums[i])
                
        return len(res)