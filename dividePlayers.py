class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # print(sum(skill))

        if sum(skill)%(len(skill)//2)!=0:
            return -1
        x=sum(skill)//(len(skill)//2)
        skill.sort()

        i=0
        j=len(skill)-1

        ans=0
        while j>i:
            if skill[i]+skill[j]!=x:
                return -1

            ans+=skill[i]*skill[j]
            i+=1
            j-=1

        return ans

