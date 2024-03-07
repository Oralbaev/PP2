import os
with open('ex2.txt', 'r') as f:
    x = sum(1 for i in f)
print(x)