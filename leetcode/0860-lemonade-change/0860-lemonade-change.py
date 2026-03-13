class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change=defaultdict(int)

        for bill in bills:
            if bill==5:
                change[5]+=1
            elif bill==10 and change[5]>=1:
                change[5]-=1
                change[10]+=1
            elif bill==20 and (change[5]>=3 or (change[10]>=1 and change[5]>=1)):
                    if change[10]>=1:
                        change[10]-=1
                        change[5]-=1
                    else:
                        change[5]-=3
            else:
                return False
        
        return True


            
