class Solution:
    def countAndSay(self, n: int) -> str:
    
        def count_say(n):
            if n==1:
                return "1"
            else:
                temp=count_say(n-1)
                ans=""
                countt=1
                for i in range(len(temp)):

                    if i==len(temp)-1 or temp[i]!=temp[i+1]:
                        ans+=str(countt)+temp[i]
                        countt=1
                    else:
                        countt+=1
                return ans
                
        return count_say(n)  