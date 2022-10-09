class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 or sum(nums[1:])==0:
            return 0
        
        
        i=0
        if n==2 and sum(nums)==0:
            return -1
        while i<n-1:
            if sum(nums[:i+1])==sum(nums[i+2:]):
                return i+1
            else:
                i+=1
        
        return -1
            
            