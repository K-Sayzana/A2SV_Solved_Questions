class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        arr_sorted=[x for x in arr]
        arr_sorted.sort()

        j=len(arr)-1

        ans=[]
        while j>=0:
            if arr_sorted[j]!=arr[j]:
                for i in range(len(arr)):
                    if arr[i]==arr_sorted[j]:
                        
                        arr[:i+1]=arr[:i+1][::-1]
                        arr[:j+1]=arr[:j+1][::-1]

                        ans.append(i+1)
                        ans.append(j+1)

                        break

            j-=1
        return ans
