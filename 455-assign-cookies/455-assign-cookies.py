class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans=0
        g.sort(reverse=True)
        s.sort(reverse=True)
        n=len(g)
        m=len(s)
        i,j=0,0
        while i<n and j<m:
            if s[j]>=g[i]:
                ans+=1
                i+=1
                j+=1
            else:
                i+=1
        return ans