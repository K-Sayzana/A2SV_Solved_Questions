x=-1
y=-1


for i in range(5):
    row=input()
   
    if '1' in row:
        x=i
        y=row.split().index('1')

print(abs(2-x) + abs(2-y))
