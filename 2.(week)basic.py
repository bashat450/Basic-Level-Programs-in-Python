# convert Celsius to Fahrenheit
'''
def farh_cel(cel):
    return cel*(9/5)+32
c=6
f=farh_cel(c)
print(f) 
'''

# Program to display calendar
'''
import calendar
yy=int(input("Enter Year: "))
mm=int(input("Enter Month: "))

print(calendar.month(yy,mm))
'''

# Program to check if a Number is Positive, Negative or Zero
'''
num = int(input("Enter a number: "))
if num<0:
    print("You can enter a number is negative...")
elif num==0:
    print("You can enter a number is zero...") 
elif num>0:
    print("You can enter a number is positive...") 
'''  

# Check if number is odd or even
'''
num=int(input("Enter a number: "))
i=num%2
if i==1:
    print(f"The {num} is odd.")
else:
    print(f"The {num} is even.") 
    ''' 

# Check Leap Year
'''
year = int(input("Enter a year: "))
if (year%4)==0:
    if (year%100)==0:
        if (year%400)==0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.") 
    '''

#Check number is prime or not
'''
num = int(input("Enter a number: "))
if num>1:
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is not a prime.")
            break
    else:
        print(f"{num} is a prime.")
else:
    print(f"{num} is not prime.")   
    '''

# Print all Prime Numbers between an Interval
'''
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num) 
'''

# Project:2 Guess a Number
import random
randNo = random.randint(1,100)
UserGuess =None
Guess = 0
while (UserGuess != randNo):
    UserGuess = int(input("Enter a number: "))
    Guess += 1
    if UserGuess == randNo:
        print("You guess the right number.")
    else:
        if UserGuess > randNo:
            print("You guess it wrong number! Please write a smaller number.")
        else:
            print("You guess it wrong number! Please write a larger number.")

print(f"You guessed the number in {Guess} guesses.")
# with open ("hiscore.txt", 'r') as f:
#     hiscore = int(f.read())

# if Guess < hiscore:
#     print("You have just broken the high score.")
#     with open ('hiscore.txt', 'w') as f:
#         f.write(hiscore)

