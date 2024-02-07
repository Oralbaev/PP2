import math
from itertools import permutations
import random

#1
def GramsToOunces(grams):
    return 28.3495231 * grams

#2
def fTC(F):
    return (F - 32) * 5 / 9

#3
def solve(numheads, numlegs):
    print("Rabits: ", (numlegs - (numheads * 2)) / 2)
    print("Chickens: ", numheads - ((numlegs - (numheads * 2)) / 2))

#4
def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def filter_prime(lst):
    return [x for x in lst if not isPrime(x)]

#5
def print_permutations(input_string):
    all_permutations = permutations(input_string)

    for perm in all_permutations:
        print(''.join(perm))

#6
def rev(s):
    lst = s.split(" ")
    res = ""
    for i in list(reversed(lst)):
        res = res + i + ' '
    return res

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3: return False
    return True

#9
def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

#10
def unique_elements(input_list):
    unique_list = []
    for x in input_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

#11
def is_palindrome(string):
    string = string.lower()
    return string == string[::-1]

#12
def is_palindrome(string):
    string = string.lower()
    return string == string[::-1]

#13
def guess_the_number():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guess = int(input("Take a guess."))
    while True:
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too much")
        else:
            print("Correct")
            break
        guess = int(input("Take a guess."))

#14
        