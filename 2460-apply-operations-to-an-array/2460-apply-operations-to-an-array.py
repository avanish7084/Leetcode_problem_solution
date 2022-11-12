class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        k,i=0,0
        while i<n-1:
            if nums[i]==nums[i+1]:
                nums[k]=nums[i]*2
                k+=1
                nums[k]=0
                k+=1
                i+=2
            else:
                nums[k]=nums[i]
                k+=1
                i+=1
        c=nums.count(0)
        num=[]
        for ele in nums:
            if ele!=0:
                num.append(ele)
        for i in range(c):
            num.append(0)
            
        return num