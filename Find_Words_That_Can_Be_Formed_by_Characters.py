class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        count=defaultdict(int)
        for ch in chars:
            count[ch]+=1
        
        ans=0
        for word in words:
            count_=defaultdict(int)
            for ch in word:
                count_[ch]+=1
            

            flag=1
            for k in count_:
                if count_.get(k, 0)>count.get(k, 0):
                    flag=0
                    break
            
            if flag:
                ans+=len(word)
        return ans
