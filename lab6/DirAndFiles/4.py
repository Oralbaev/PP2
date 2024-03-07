import os
S = 0
with open('ex2.txt', 'r') as f:
    for x in f: S += 1
print(S)