class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        while original in nums:
            original*=2
        return original
    
    
#         nums.sort()
#         if len(nums)==1 and nums[0]==original:
#             return original*2
#         if len(nums)==1:
#             return original
#         def search(arr,t):
#             s=0
#             e=len(arr)-1
#             res=-1
#             while s<=e:
#                 mid=(s+e)//2
#                 if arr[mid]==t:
#                     return True
#                 elif arr[mid]<t:
#                     s=mid+1
#                 else:
#                     e=mid-1
#         res=0
#         for i in range(len(nums)):
#             if search(nums,original):
#                 original=original*2
#                 continue 
#             else:
#                 return original
            
        
                