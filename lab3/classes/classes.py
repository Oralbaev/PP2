import math

#1
class String:
    def __init__(self) -> None:
        self.input_string = ""

    def getString(self):
        self.input_string = str(input())

    def printString(self):
        print(self.input_string.upper())


#2, 3        
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2


class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

#4
class Point():
    def __init__(self, x, y):
        self.x1 = x
        self.y1 = y
    
    def show(self):
        return self.x1, self.y1
    
    def move(self, x, y):
        self.x1 = x
        self.y1 = y
    
    def dist(self, x, y):
        return (int(math.sqrt((x - self.x1) **2 + (y - self.y1) ** 2)))


#5
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, num):
        self.balance += num
        print(f"Deposit of {num} successful. Current balance: {self.balance}")
    def withdraw(self, num):
        if num > self.balance:
            print('Not enough money')
        else:
            self.balance -= num
            print(f"Withdrawal of {num} successful. Current balance: {self.balance}")

#6
def IsPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True