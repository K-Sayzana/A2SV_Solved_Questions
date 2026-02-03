class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        i=0
        flag=0
        ans=""

        
        min_size=len(min(strs, key=len))
        while (not flag and i < min_size):
            lett = set() 
            for word in strs:
                lett.add(word[i])
            if(len(lett)==1):
                ans+=lett.pop()
                i+=1
            else:
                flag=1
        
        return ans



