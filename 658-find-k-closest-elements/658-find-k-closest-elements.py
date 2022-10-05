class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d=[]
        for i in arr:
            d.append([i,abs(x-i)])
            
        d.sort(key=lambda x:x[1])
        ans=[]
        for i in range(k):
            ans.append(d[i][0])
        ans.sort()
        return ans
            
        