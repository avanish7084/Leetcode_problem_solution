class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        ana_dict={}
        for s in strs:
            c=''.join(sorted(s))
            if c in ana_dict:
                ana_dict[c].append(s)
            else:
                ana_dict[c]=[s]
        
        print(ana_dict)   
        for i in ana_dict:
            res.append(ana_dict[i])
        return res 
        