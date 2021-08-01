# Find the Factorial of a number
'''
num = int(input("Enter a number: "))
factorial = 1
if num<0:
    print("Please, Enter a positive number.")
elif num == 0:
    print("The factorial of a 0 is 1.")
elif num>0:
    for i in range(1,num+1):
        factorial = factorial*i
    print(f"The factorial of a {num} is {factorial}")
    ''' 

# Display the multiplication table
'''
n = int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}") 
    '''
    
# Print the Fibonacci sequence
'''
n=int(input("How many terms you want: "))
a=0
b=1
c=2
if n<=0:
    print("Invalid number..Enter a positive number.")
elif n==1:
    print("Fibonacci series ")
    print(a)
else:
    print("Fibonacci series ")
    print(a,",",b,end=',')
    while c<n:
        d=a+b
        print(d,end=',')
        a=b
        b=d 
        c+=1
        '''
        # &&&&
'''        
def fibonacci(n):
    a=0
    b=1
    if n<0:
        print("Invalid number.")
    elif n==0:
        return 0
    elif n==1:
        return b
    else:
        for i in range(1,n):
            c=a+b  
            a=b
            b=c
        return b
print(fibonacci(12))
'''
                    # &&&& 
'''                     
def fib(n):

    if n < 0:
        print("Invalid number.") 
    elif n == 0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n+2) 
print(fib(9))  
'''

# Program to Check Armstrong Number
'''
num = int(input("Enter a number: "))
sum=0
temp = num
while temp>0:
    digit = temp % 10
    sum += digit**3
    temp //= 10
if num == sum:
    print(f" {num} is a Armstrong number.") 
else:
    print(f"{num} is not a Armstrong Number.") 
    '''

# Program to Find Armstrong Number between an Interval
'''
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower,upper+1):
    sum = 0
    temp = num
    while temp>0:
        digit = temp % 10
        sum += digit**3
        temp //= 10
        if num == sum:
            print(num)
            '''

# Program to Find the Sum of Natural Numbers
'''
num=int(input("Enter a number: "))
if num<0:
    print("Enter a positive no.: ")
else:
    sum=0
    while num>0:
        sum+=num
        num-=1
    print(f"The sum is {sum}.")  
    '''

# Program Alarm Clock with GUI  
from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%y")
        print(f"The Set Date is: {date}.")
        print(now)
        if now == set_alarm_timer:
            print(" Time to wake up ")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
      

clock = Tk()

clock.title("DataFlair Alarm Clock")
clock.geometry("400x250")
time_format=Label(clock,text="Enter time in 24 hour format!", fg="white", bg="black",font="Arial").place(x=80,y=160)
addTime = Label(clock,text = "Hour Min Sec", font=60).place(x=0, y=29)
setYourAlarm = Label(clock,text = "When to wake you up",bg="black" ,fg="red", relief = "solid", font=("Helevetica",15,"bold")).place(x=110, y=60)

# The Variable we require to set the alarm (initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

# Time required to set the alarm clock:
hourTime = Entry(clock,textvariable=hour,bg="pink",width = 15).place(x=110,y=30)
minTime = Entry (clock,textvariable=min, bg="pink", width = 15).place(x=150, y=30)
secTime = Entry(clock, textvariable=sec, bg="pink", width = 15).place(x=200,y=30)

# To take the time input by the user:
submit = Button(clock, text = "Set Alarm",fg="red",width = 10, command= actual_time).place(x=150,y=110)

clock.mainloop()





                 