class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        
        for i in range(len(nums)):
            l=list(str(nums[i]))
            
            for j in l:
                res.append(int(j))
        return res