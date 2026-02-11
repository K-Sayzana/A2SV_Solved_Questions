class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1)!=len(word2) or len(set(word1)-set(word2))!=0:
            return False

        count1 =Counter(word1)
        count2 =Counter(word2)

        a=[]
        b=[]

        for val in count1.values():
            a.append(val)
        for val in count2.values():
            b.append(val)

        a.sort()
        b.sort()

        if a==b:
            return True
        return False
        
        
