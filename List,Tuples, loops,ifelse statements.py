
#Mad libs game

color=input("Enter a color :")
animal=input("Enter an animal name :")
Celebrity=input("Enter a Celebrity :")


print("Roses are " + color)
print("Pink " + animal)
print("I am " + Celebrity)



#LISTS
#Structure inside a python to store bunch of information
Superheroes=["Ironman","Batman","Spiderman","Aquaman","Thor"]

#LISTS can store more than 1 value and can have multiple value types(Boolean, Integers etc)
print(Superheroes)

#INDEX
#Use it to identify the value based on the position
print(Superheroes[1] + "&"+ Superheroes[2])

#Use negative to retrieve the value backwards
print(Superheroes[-1])

#and get portions of the list
print(Superheroes[1:3])

Superheroes[2]="Wolverine"
print(Superheroes[1:])


#LIST Functions
numbers=[2,4,6,17,89]
Superheroes=["Ironman","Batman","Spiderman","Aquaman","Thor"]

print(Superheroes)


#Extend-Add existing list
Superheroes.append(numbers)
print(Superheroes)


#Append-Add more details, can be custom
Superheroes.append("Black widow")
print(Superheroes)

#INSERT function to add value in between as per the Index position
Superheroes.insert(6,"Captain America")

print(Superheroes)

#Remove elements
Superheroes.remove("Captain America")
print(Superheroes)

#Clear everythinhg
Superheroes.clear()
print(Superheroes)

#POP-removes the last element in the list
Superheroes.pop()
print(Superheroes)

#index search
print(Superheroes.index("Samir"))

#Count
print(Superheroes.count("Ironman"))

#Sort
Superheroes.sort()
print(Superheroes)

#Copy
Superheroes2=Superheroes.copy()
print(Superheroes2)

print(
Superheroes + Superheroes2)


#TUPLES- type of container where you can store multiple pieces of information
#Tuples cannot be changes -IMMUTABLE
coordinates=(4,5)
print(coordinates[1])

###coordinates1=[(12,13),(2,3),(3,4)]

#FUNCTIONS -helps in organizing the code
def say_hi():
    print("Hello user")#Code going inside the function needs to be idented

say_hi()

#PARAMETERS- piece of information given to the function
def greet(name, age):
    print("Hello " + name + ", You're " + age)
greet("Mike", "35")
greet("Tony","30")




#Return statement
def cube(num):
    return num*num*num    #Python recognized the return function as the result the user is requesting
result=cube(3)

print((result))



#If statements
#mostly used in conditional statements. Example: if it rains then I am not stepping out    OR If it is rainy I might not come otherwise I will come

is_male=False
is_tall=True
if  is_male and is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):      #not is used to check if that condition is met or not
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are neither male nor tall")


#if statements and comparisions

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))


#Building a better calculator
num1= float(input("Enter first number: "))
op= input("Enter operator: ")
num2= float(input("Enter second number: "))

if op == "+":
    print(num1 +num2)
elif op=="-":
    print(num1-num2)
elif op=="/":
    print(num1/num2)
elif op=="*":
    print(num1*num2)
else:
    print("Invalid operator")





#DICTIONARIES
month_conversions={
    "Jan": "January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "October": "October",
    "Nov": "November",
    "Dec":"December"
}

print(month_conversions)
print(month_conversions["Mar"])

print(month_conversions.get("Ohh","Not a valid key"))


####LOOPS

#while loop
i=1     #define the variable
while i<=10:    #condition- will loop as long as the condition is true
    print(i)  #print the condition
    i=i+1  #mention the iteration, like +1, +2 etc

print("loop is done")

#Guessing game
secret_Word="Giraffe"           #winning word
guess=""                        #user input
guess_count=0                   #count of user guessing
guess_limit=3       #How many times, user can limit
out_of_guesses=False

while guess!= secret_Word and not(out_of_guesses):
    if guess_count< guess_limit:
        guess=input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses=True

if out_of_guesses:
    print("You lose !")
else:
print("You win !")


#For loops

for letter in "Queens gambit":
    print(letter)

friends=["Jim","cliff","Sam"]
for name in friends:
    print(name)

for ranges in range(len(friends)):
    print(ranges)

for num in range(3,10):
    print(num)


#More loops in practice
number=[1,2,3,4,5]
fruits=['apple','grapefruit','pears']

for anything in number:
    print(f"this is count {anything}")

for fruit in fruits:
    print(f"{fruit} is my favorite")

for ranges in range(len(fruits)):
    print (ranges)

change=[1,'penny',2,'dimes',3,'Quarters']

for anything_else in change:
    print(f'I have {anything_else}')


#Filling out an empty string
elements=[]

for i in range(0, 6):
    print(f"Adding {i} to the list")
#Appending the numbers to the list
elements.append(i)

for i in elements:
    print(f"{i} was the element")


#While loop- Will keep executing until the boolean expression is true
i=0
numbers=[]

while i<6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i=i+1
    print("numbers now: ",numbers)








#Exponent function
print(2**3)

def raise_to_power(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result=result * base_num
    return result

print(raise_to_power(2,3))

#2D list
number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid)

print(number_grid[0][0])

#Nested for loop
for rows in number_grid:
    for columns in rows:
        print(columns)



#Build a translator
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation=translation + "G"
            else:
                translation=translation+ "g"

        else:
            translation=translation+letter
    return translation

print(translate(input("Enter a phrase:")))


#TRY EXCEPT
try:
    number=int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")



 #If we want to specify the error type
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Div. by zero")
except ValueError:
    print("invalid input")



#Reading from external file
file=open("/Users/Samir/Desktop/Dave,Samir.pdf","r")

file.close()
# r read
# w write
#a append

#complete read and write modules



#modules in pip
# save the file by any desired name and include the python functions and other details
import useful_tools
import useful_tools





