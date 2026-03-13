class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles==0:
            return target-1

        ans=0
        while target>1:
            if target%2==0 and maxDoubles>0:
                target//=2
                maxDoubles-=1

                if maxDoubles==0:
                    return ans + target
            else:
                target-=1
            ans+=1 
        

        return ans