class Solution:
    def maximum69Number (self, num: int) -> int:
        ans=""
        f=0
        num=str(num)
        for i in num:
            if i=="6" and f==0:
                ans+="9"
                f=1
            else:
                ans+=i
        return ans
            
                