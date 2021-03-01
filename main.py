# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Use ctrl+shift+E to run the selected code

print("Hello,This is your first program")
print("There was a man named George")
print("He was around 70 years old")
print("He liked everything except being old which was 70 years")

 #Variables
 #Lets Say you want to change the name and age. Declare the variable and then it can be called in the statements
character_name="John"  #String values
character_age="35"  #Numeric values
is_Male=True #Boolean values
print("Hello,This is your first program")
print("There was a man named " + character_name + ",")
print("He was around" + character_age + "years old")
print(character_name + "is a great man")
print("He liked everything except being old which was 70 years")


#Working with strings
print("Samir's \n  den")
print("Samir's \"  den") #To print the quotation mark

#Declare the print statement in a variable
phrase="Diversity"
print(phrase + " is our biggest strength")

#FUNCTIONS
print(phrase.lower())  #To get lower case
print(phrase.upper())  #To get upper case
print(phrase.islower())  #To get values(Boolean) of the variable. Answer is False in our case because it is not lowercase
print(phrase.lower().islower()) #Convert it first to get the true value
print(len(phrase)) # Length of the string
print(phrase[8]) #get the characters
#NOTE- The String gets indexed starting with 0.
#Diversity
#012345678
#so the word Diversity will have D as 0 and Y as 8

#Index function will get us the position of the word. Can be used to get words as well
print(phrase.index('s'))
print(phrase.index('sity'))

#Replace function will replace the words as mentioned in the string
print(phrase.replace("sity","sification"))


#Working with numbers
print(2.08474 - 3) #can use + - *

print(3 * 4 + 5) # It will execute in the order it was received

print(3* (4+5)) #Mention the order of operations

print(10 % 4)  #This modulus operator can get us the remainder

my_num=5
print(my_num+3)
print(my_num+78)

#To convert it into string- We need to convert it into string to merge it with the string
print(str(my_num+3) + " is an even number")

#FUNCTIONS in a number
number=-5
print(abs(number))  #Absolute

print(pow(3,5))  #Power 3 to the power of 5

print(max(2,2.5))  #print the maximum value of numbers

print(min(2,2.5,1))   #Print the minimun value of numbers

print(round(3.5))  #Rounding off on the numbers

#Import other math functions that are not already existing
from math import *
print(floor(3.5))  #Get the lowest value
print(ceil(3.5))  #Get the highest value
print(sqrt(81))  #Get the square root

