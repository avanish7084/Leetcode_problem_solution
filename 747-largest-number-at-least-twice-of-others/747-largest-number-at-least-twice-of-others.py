class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first_max=nums[0]
        second_max=-1
        idx=0
        for i in range(1,len(nums)):
            if first_max<nums[i]:
                first_max=nums[i]
                idx=i
        
        for i in range(len(nums)):
            if nums[i]>second_max and nums[i]<first_max:
                second_max=nums[i]
        
        print(first_max,second_max)
                
        if (2*second_max)<=first_max:
            return idx
        else:
            return -1