class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
#         ana={}
#         for i in words:
#             s="".join(sorted(i))
#             if s in ana:
#                 continue
#             else:
#                 ana[s]=i
#         l=ana.values()
        
#         return l

        output=[words[0]]
        for i in range(1,len(words)):
            val1 = "".join(sorted(words[i]))
            val2 = "".join(sorted(words[i-1]))
            if val1 != val2:
                output.append(words[i])
        return output