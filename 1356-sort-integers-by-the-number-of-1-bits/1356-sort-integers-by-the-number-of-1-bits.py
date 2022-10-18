class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        temp=[]
        for num in arr:
            num_in_binary=bin(num)
            temp.append([num_in_binary.count('1'),num])
            
        temp.sort()
        ans=[]
        
        for freq,num in temp:
            ans.append(num)
            
        return ans
    
      
        
        
        
        
        
        
        
#         arr.sort()
#         n=len(arr)
#         m,o=[],[]
#         for i in range(n):
#             k=arr[i]
#             if (k & (k-1))==0:
#                 m.append(k)
#             else:
#                 o.append(k)
#         return m+o
                