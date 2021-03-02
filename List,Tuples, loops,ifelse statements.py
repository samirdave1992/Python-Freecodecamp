
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