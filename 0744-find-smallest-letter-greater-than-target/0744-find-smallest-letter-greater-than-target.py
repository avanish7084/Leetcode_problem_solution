class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        char=""
        char_d=1000
        for i in letters:
            if (ord(i)-ord(target))>0 and char_d>(ord(i)-ord(target)):
                char_d=(ord(i)-ord(target))
                char=i
        if len(char)==0:
            return letters[0]
        return char