class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        ans=0
        
        i=0
        j=n-1

        while j>=i:
            
            if people[i]+people[j]<=limit:
                i+=1
                j-=1
            else:
                j-=1

            ans+=1
        return ans
