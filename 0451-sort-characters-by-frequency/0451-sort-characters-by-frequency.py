class Solution:
    def frequencySort(self, s: str) -> str:
        h={}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        h=sorted(h.items(), key=lambda x: x[1])
        res=""
        for i in range(len(h)-1,-1,-1):
            
            res+=h[i][0]*h[i][1]
            
        return res