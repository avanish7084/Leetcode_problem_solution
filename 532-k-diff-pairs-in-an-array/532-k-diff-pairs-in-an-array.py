class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        # Brute_force Approach 
        
        # n=len(nums)
        # s=set()
        # nums.sort()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if abs(nums[i]-nums[j])==k:
        #             s.add((nums[i],nums[j]))
        #             print(s)
        # return len(s)
        
        # Optimal
     
        n=len(nums)
        ans=0
        nums.sort()
        s,e=0,1
        while (e<n and s<n):
            
            if s>=e:
                e=e+(s-e)+1
                continue
                
            diff=nums[e]-nums[s]
            
            if diff<k:
                e+=1
            elif diff>k:
                s+=1

            else:
                
                ans+=1
                s+=1
                
                while s<n and nums[s]==nums[s-1]:
                    s+=1
            
        return ans