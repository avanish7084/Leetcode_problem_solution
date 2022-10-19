class Solution:
    def topKFrequent(self, words: List[str], l: int) -> List[str]:
        d,k={},{}
        for i in words:
            if i in d:
                
                d[i]+=1 
            else:
                
                d[i]=1
            
        k=sorted(d.items(),key=lambda item:item[1],reverse=True)
        
        n=len(k)
        temp,p,res=[],[],[]
        
        p.append(k[0])
        
        for i in range(1,n):
            if k[i][1]!=p[-1][1]:
                p.sort()
                for j in range(len(p)):
                    temp.append(p[j])
                p=[]
                p.append(k[i])
            else:
              print(i)
              p.append(k[i])
            
        p.sort()
        for i in range(len(p)):
            temp.append(p[i])
        
        for i in range(l):
            res.append(temp[i][0])
        return res