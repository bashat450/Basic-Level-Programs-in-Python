# Question-1
# This function converts miles to kilometers (km).
'''

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km
miles = 55
# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(miles)
print("The distance in kilometers is " + str(my_trip_km))
print("The round-trip in kilometers is " + str(my_trip_km*2))
'''



# Question-2
# This function compares two numbers and returns them in increasing order.
# This function compares two numbers and returns them in increasing order. 
'''
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1
(smaller, bigger) = order_numbers(100, 99)
print(smaller, bigger)
'''


# Question-3
# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one 
# byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 
# bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function 
# below, which calculates the total number of bytes needed to store a file of a given size?
'''
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size*(full_blocks+1)
    return block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
'''

# Question-4
#  The longest_word function is used to compare 3 words. It should return the word with the
#  most number of characters (and the first in the list when they have the same length).
'''
def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word1) <= len(word2) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))  
'''

# Question-5
#  The fractional_part function divides the numerator by the denominator, and returns just the 
# fractional part (a number between 0 and 1). Complete the body of the function so that it 
# returns the right number. Note: Since division by 0 produces an error, if the denominator is 
# 0, the function should return 0 instead of attempting the division.
'''
import math
def fractional_part(numerator, denominator):
	if denominator == 0:
 	    return 0
	return numerator / denominator - math.floor(numerator / denominator)
print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0 
'''

# Question-6
# check if the given number is a Disarium Number
#calculateLength() will count the digits present in a number  
'''  
def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
num = 172;  
# num = 175  
rem = sum = 0;    
len = calculateLength(num);    
     
#Makes a copy of the original number num    
n = num;    
     
#Calculates the sum of digits powered with their respective position    
while(num > 0):    
    rem = num%10;    
    sum = sum + int(rem**len);    
    num = num//10;    
    len = len - 1;    
     
#Checks whether the sum is equal to the number itself    
if(sum == n):    
    print(str(n) + " is a disarium number");    
else:    
    print(str(n) + " is not a disarium number");  

	'''



# Mad Libs Generator Game
from tkinter import *
# initialize window
root = Tk()
root.geometry('300x300')
root.title('DataFlair-Mad Libs Generator')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()
Label(root, text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)
################Stories##############

def madlib1():
    animals= input('enter a animal name : ')
    profession = input('enter a profession name: ')
    cloth = input('enter a piece of cloth name: ')
    things = input('enter a thing name: ')
    name= input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('food name: ')
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken today. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + ' .when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')
def madlib2():
    adjactive = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')
    print('Last night I dreamed I was a ' +adjactive+ ' butterfly with ' + color+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjactive1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')
def madlib3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')
    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')  

######buttons   
Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'apple and apple', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=70, y=180)
Button(root, text= 'The Butterfly', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)

root.mainloop()

