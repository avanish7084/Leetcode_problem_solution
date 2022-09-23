class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        #methode 3
        
        # method 2
        
        
        ans=""
        for i in range(1,n+1):
            ans+=format(i,'b')
            
        res=int(ans,2)%(10**9+7)
        
        return res
        
        
        
        #method 1 ---->>> which is gives us Tle
        
#         def convert_binary(n):
#             s = ""
#             while n >= 1:
#                 if n == 1:
#                     s += str(1)
#                     n -= 1
#                     continue
#                 r = n % 2
#                 s += str(r)
#                 n = n // 2
#             return s[::-1]


#         def convert_decimal(s):
#             s=s[::-1]
#             ans = 0
#             n = len(s)
#             for i in range(n):
#                 ans += int(s[i])*(2**i)
#             return ans
        
#         string=""
#         for i in range(1,n+1):
#             string+=convert_binary(i)
#         return convert_decimal(string)%(10**9+7)
        
        
        
        