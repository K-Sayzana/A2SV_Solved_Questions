class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        con=defaultdict(list)
        for path in paths:
            line=path.split()
            for i in range(1, len(line)):
                content=line[i].split('(')
                con[content[1][:-1]].append(line[0]+'/'+content[0])
        

        ans=[]
        for k, v in con.items():
            if len(v)>1:
                ans.append(v)
        return ans

