class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1],[1,1]]
        for r in range(2,numRows+1):
            temp=[1]
            
            for c in range(1,r-1):
                s=res[r-1][c-1]+res[r-1][c]
                temp.append(s)
            temp.append(1)
            res.append(temp)
                
                
            
            
        return res[:1]+res[2:]