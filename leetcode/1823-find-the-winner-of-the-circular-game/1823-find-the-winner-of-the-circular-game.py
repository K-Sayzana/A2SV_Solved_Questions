class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k==1:
            return n
        plys=[x for x in range(1, n+1)]
        def play(i, c, plys):
            if len(plys)==1:
                return plys[0]
            if c>=k:
                c=1
                plys.pop(i)
                # print(plys)
            
            return play((i+1) % len(plys), c+1, plys)
        
        return play(0, 1, plys)
            
