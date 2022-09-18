class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        good_pair=0
        d={}
        for u in range(n):
            a=nums[u]-u
            if a in d:
                d[a]+=1
            else:
                d[a]=1
        print(d)
        good_pair=0
        total_pair=(n*(n-1))//2
        for i in d:
            
            good_pair+=(d[i]*(d[i]-1))//2
            
            
        print(good_pair,n)
        
        return total_pair-good_pair