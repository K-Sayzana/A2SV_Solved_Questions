class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count=defaultdict(int)

        for i in range(len(responses)):
            unique=set(responses[i])
            for res in unique:
                count[res]+=1

        count_=[]
        for k, v in count.items():
            count_.append((v,k))
        
        count_.sort(reverse=True)
        
        ans=[]
        curr_max=count_[0][0]
        
        for cou in count_:
            if cou[0]==curr_max:
                ans.append(cou[1])
            else:
                break


        ans.sort()

        return ans[0]

