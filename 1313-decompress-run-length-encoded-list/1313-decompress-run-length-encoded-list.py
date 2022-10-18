class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
      
        for i in range(0,len(nums),2):
            k=i+1
            j=0
            while j<nums[i]:
                ans.append(nums[k])
                j+=1
        
        return ans
            
            