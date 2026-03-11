class Solution:
    def decodeString(self, s: str) -> str:
        
        stack_num=[]
        stack_ans=[]

        curr_num=0
        for ch in s:
            if ch.isdigit():
                curr_num= curr_num * 10 + int(ch)
            elif ch =='[':
                stack_num.append(curr_num)
                curr_num=0
                stack_ans.append(ch)
            elif ch==']':
                temp=[]
                while stack_ans and stack_ans[-1]!='[':
                    temp.append(stack_ans[-1])
                    stack_ans.pop()
                
                part="".join(reversed(temp)) * stack_num.pop()
                stack_ans.pop() 
                stack_ans.append(part)
            else:
                stack_ans.append(ch)
            

        return "".join(stack_ans)

                