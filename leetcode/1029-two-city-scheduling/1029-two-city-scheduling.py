class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)//2
        costs.sort(key=lambda x: abs(x[0]-x[1]), reverse=True)

        print(costs)
        a, b=0, 0
        ans=0
        for cost in costs:
            if (b==n) or( cost[0]<=cost[1] and a < n):
                a+=1
                ans+=cost[0]
            else:
                b+=1
                ans+=cost[1]
        # print(a)
        return ans
        

                

        