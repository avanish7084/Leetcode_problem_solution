class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        s=0
        for r in range(n):
            for c in range(n):
                if r==c:
                    s+=mat[r][c]
                if (r+c)==n-1:
                    s+=mat[r][c]
        if len(mat)%2!=0:
            k=len(mat)//2
            s=s-mat[k][k]
      
        return s