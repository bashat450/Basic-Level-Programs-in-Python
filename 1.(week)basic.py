# Print Hello
# print(f'Hello, Bashat nice to see you again!' )

# arithematic operator
'''a=5
b=3
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} x {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} > {b} = {a>b}")
print(f"{a} < {b} = {a<b}")
print(f"{a} | {b} = {a|b}")
print(f"{a} modules {b} = {a%b}")
print(f"{a} increment {b} = {a++b}")
print(f"{b} decrement {a} = {b--a}")'''

# Area of triangle
# formula = (b)base*(h)height/2
'''b=5
h=6
t=b*h
a=t/2
print(f"The area of the triangle is {a}.")'''

# Quadratic equation
# Formula = (-b+root of (b(square)-4ac))/(2a)  && (-b-root of (b(square)-4ac))/(2a)
'''
import math
b=9
a=4
c=2
Q=(-b+ math.sqrt(b**2-4*a*c))/(2*a)
E=(-b- math.sqrt(b**2-4*a*c))/(2*a)
print(f"The Quadratic Equation of + (positive number) is {Q} .")
print(f"The Quadratic Equation of - (negative number) is {Q} .")
'''

# Swap two variable
'''
a=5
b=10
c=a
a=b
b=c
print(f"The value of a after swapping is {a} .")
print(f"The value of b after swapping is {b} .")
'''

# Generate a random number
'''
from random import randint
value =randint(0,10)
print(value)
'''
#  &&
'''
from random import seed
from random import randint
seed(1)
for i in range(10):
    value = randint(0,10)
    print(value)
'''
'''
import random
randNo = random.randint(0,10)
print(randNo)
'''
# Convert kilometers to miles
# kilometers = miles / ratio & conv_fac
# miles = kilometers * ratio & conv_fac
'''
kilometers = float(input("Enter value in kilometers: "))
ratio = 0.621371
miles = kilometers*ratio
print("%0.2f is equal to %0.2f " %(kilometers,miles))
'''

# First week project ..................
# GAME [Snake, Water And Gun] &&& Same game as [Stone, Paper, Scissor]
import random
def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False 
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False  

# print("computer choice is : Snake (s), Water(w) and Gun(g) ")
randNo = random.randint(1,3)
if randNo == 1:
    comp='s'
elif randNo == 2:
    comp='w'
elif randNo == 3:
    comp='g' 

you = input("Enter your choice : Snake (s), Water(w) and Gun(g) = ")

a=gameWin(comp,you)

print(f"Computer choose : {comp}")
print(f"You choose : {you}")

if a==None:
    print("Computer and you can choose same item, That's why ...This game is Tie ")
elif a:
    print("Congrats, You Win the game.")    
else:
    print("Oops, You loose the game, Try again....")    