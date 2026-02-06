class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grp=defaultdict(list)
        for word in strs:
            grp["".join(sorted(word))].append(word)
        

        ans=[]

        for v in grp.values():
            ans.append(v)
        return ans
            
