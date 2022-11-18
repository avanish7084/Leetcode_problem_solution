class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])

        mat=[x[:] for x in matrix]
        for r in range(n):
            for c in range(m):
                if mat[r][c]==0:
                    for change_col in range(m):
                        matrix[r][change_col]=0
                        print(r,change_col)
                    for change_row in range(n):
                        matrix[change_row][c]=0
        
            
        