class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[[]]
        curr=2001

        for i in range(len(list1)):
            s=list1[i]
            if s in list2:
                idx=list2.index(s)

                if idx+i<curr:
                    ans.append([])
                    ans[-1].append(s)
                    curr=idx+i
                elif idx+i==curr:
                    ans[-1].append(s)

       
        return ans[-1]
