# Program to Find LCM
'''
num1 = int(input("Enter a 1st no.: "))
num2 = int(input("Enter a 2nd no.: "))
def calculate_lcm(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    while True:
        if (greater%x==0)and(greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm
print(f"The LCM of {num1} and {num2} is {calculate_lcm(num1,num2)} .") 
'''

# Program to Find LCM
'''
num1 = int(input("Enter a 1st no.: "))
num2 = int(input("Enter a 2nd no.: "))

def calculate_hcf(x,y):
    if x>y:
        greater = y
    else:
        greater = x
    for i in range(1,greater+1):
        if (x%i==0)and (y%i==0):
            hcf = i
       
    return hcf
print(f" The HCF of {num1} and {num2} is {calculate_hcf(num1,num2)} .")  
'''

# Program to Convert Decimal to Binary, Octal and Hexadecimal
'''
dec = int(input("Enter a decimal nuber: "))
print(bin(dec),"in binary.")
print(oct(dec)," in Octal.")
print(hex(dec)," in hexadecimal.")
'''

# Program To Find ASCII value of a character
'''
char = input("Enter a character: ")
print(f"The ASCII value of {char} is ",ord(char))
'''

# Program to Make a Simple Calculator
'''
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def divide(x,y):
    return x/y

print("...Select Option.........")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Divide")

choice = int(input("Enter a choice (1/2/3/4)."))
num1 = int(input("Enter a 1st number: "))
num2 = int(input("Enter a 2nd number: "))

if choice == 1:
    print(f"{num1} + {num2} = ",add(num1,num2))
elif choice == 2:
    print(f"{num1} - {num2} = ", subtract(num1,num2)) 
elif choice == 3:
    print(f"{num1} * {num2} = ", multiplication(num1,num2))  
elif choice == 4:
    print(f"{num1} / {num2} = ", divide(num1,num2)) 
else:
    print("Invalid number.")  
    '''

# Program to Display Fibonacci Sequence Using Recursion
'''
def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))    
nterms = int(input("How many terms? "))    
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i))  
       '''

# Program to Find Factorial of Number Using Recursion
'''
def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)    
num = int(input("Enter a number: "))    
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num)) 
   '''

#  Welcome to DataFlair Hangman Game:
import random
import time
# Initial Steps to invite in the game:
print("\nWelcome to Hangman game by DataFlair\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)
# The parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
# A loop to re-execute the game when the first round ends:
def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()
# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()
main()
hangman()   