class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        maped=defaultdict(str)

        if len(list(pattern)) != len(s.split()):
            return False

        if len(set(list(pattern))) == len(pattern) and len(s.split())==len(set(s.split())):
            return True

        # print()
        
        patt=list(pattern)
        words=s.split()


        for k, v in zip(patt, words):
            if maped.get(k, "") == "" and maped.get(v, "") == "":
                maped[k]=v
                maped[v]=k
            elif maped.get(k)!=v or  maped.get(v)!=k:
                return False
        

        return True
