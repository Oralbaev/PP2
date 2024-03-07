import os
f = open('ex2.txt', 'r')
with open('ex1.txt', 'w') as file:
    for x in f:
        file.write(x)

f.close()