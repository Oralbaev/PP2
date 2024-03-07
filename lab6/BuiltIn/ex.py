#1
l = [int(el) for el in input().split()]
print(eval('*'.join(str(item) for item in l)))

#2
s = input()
upp = sum(map(lambda a : a.isupper(), s))
low = sum(map(lambda a : a.islower(), s))
print(f"Upper case letters: {upp} \nLower case letters: {low}")

#3
s = input()
s1 = "".join(reversed(s))
if s == s1:
    print("YES")
else:
    print("NO")

#4
def custom_sleep(n, delay): 
    start_time = 0 
    while start_time <=  delay: 
        start_time += 0.000051 
    return n**(1/2)
print("Input: ")
n = int(input())
delay = int(input())
print(f"Square root of {n} after {delay} is {custom_sleep(n, delay)}")

#5
t = (1, 2, 3)
print(all(t))









