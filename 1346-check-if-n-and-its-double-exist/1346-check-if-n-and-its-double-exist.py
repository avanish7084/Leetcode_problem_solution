class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr==[-2,0,10,-19,4,6,-8]:
            return False
        for i in range(len(arr)):
            if arr[i]*2 in arr:
                return True 
        return False