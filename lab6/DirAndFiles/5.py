import os
lst = list(input().split())
with open('ex2.txt', 'w') as f:
    for i in lst:
        f.write(str(i)+'\n')