class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine)<len(ransomNote):
            return False
        

        count1=Counter(magazine)
        count2=Counter(ransomNote)

        for k, v in count2.items():
            if count1.get(k, 0) < v:
                return False
        

        return True
