class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = {}
        res = 0
        for w in words:
            temp = w[::-1]
            if temp in d and d[temp] > 0:
                d[temp] -= 1
                res += 4
            else:
                d[w] = d.get(w, 0) + 1
        for i in d:
            if i == i[::-1] and d[i] > 0:
                return res+2
        return res