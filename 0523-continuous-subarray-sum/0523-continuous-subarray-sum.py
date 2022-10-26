class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_d={0:-1}
        rem=0
        for i,j in enumerate(nums):
            rem=(rem+j)%k
            if rem in rem_d:
                if rem_d[rem]<i-1:
                    return True
            else:
                rem_d[rem]=i
                
        return False