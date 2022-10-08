class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        nums=boxTypes
        nums.sort(key=lambda x:x[1],reverse=True)
        ans=0
        i=0
        while truckSize>0 and i<len(nums): 
            numberOfBoxes=nums[i][0]
            print(numberOfBoxes)
            while numberOfBoxes>0 and truckSize>0:
                ans+=nums[i][1]
                numberOfBoxes-=1
                truckSize-=1
            i+=1
        return ans
                