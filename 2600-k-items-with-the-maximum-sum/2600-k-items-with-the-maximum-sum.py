class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if (numOnes-k)>=0:
            return k
        
        elif (k-numOnes-numZeros)<=0:
             return numOnes
        elif (numOnes-numZeros-k)<0:
            summ=0
            summ=+numOnes
            k=k-numOnes
            k=k-numZeros
            for i in range(k):
                summ-=1
            
            return summ
       
            
            
            