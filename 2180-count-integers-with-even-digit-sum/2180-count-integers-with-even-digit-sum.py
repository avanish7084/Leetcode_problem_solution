class Solution:
    def countEven(self, num: int) -> int:
        count_even=0
        
        for i in range(1,num+1):
            l=list(str(i))
            s=0
            for j in l:
                s+=int(j)
            if s%2==0:
                count_even+=1
        return count_even
        