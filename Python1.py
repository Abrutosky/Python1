#Alex Brutosky - Python basics

#Strings
print("Hello, world!")
print('Hello, world!')
print("""This string runs
multiple lines!""")
print("This string is "+"awesome!") #we can also concatenate
print('\n') #new lines
print('Test that new line out.')

#Math
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left over
print(50 / 6) division with decimals
print(50 // 6) #no remainder

#Variables
quote = "All is fair in love and war"
print(quote)

#Methods
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters

#Numbers
name = "Alex" #string
age = 24 #int
gpa = 3.7 #float - has a decimal

print(int(age))
print(int(30.1)) #->this rounds down to 30
print(int(30.9))  #-> this rounds up to 40

print("My name is " + name + " and I am " + str(age) + "years old.")

age +=1
print (age)

birthday = 1
age += birthday

#Functions
print("Here is an example function:")

def who_am_i(): #this is a function without parameters
	name = "Alex"
	age = 24 #local variable
	print("My name is " + name + "and I am " + str(age) + " years old.") 

who_am_i()

#adding paramters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred()

#multiple parameters
def add(x,y):
	print(x + y)

add(y,y)

def multiply(x,y)
	return x * y

def square_root(x):
	print(x ** .5)

	square_root(64)


def nl():
	print('\n')

nl()


#Boolean expressions (True or False)
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

#Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
great_than_equal_to = 7 >=7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False

#Conditional Statements
def pizza(money):
	if money >= 2:
		return "You can afford pizza!"
	else:
		return "Looks like somebody's not getting any pizza :("

print(pizza(3))
print(pizza(1))

def beer(age,money):
	if(age >= 21) and (money >= 5):
		return "You can buy beer!"
	elif (age >= 21) and (money < 5):
		return "You can't afford any beer"
	elif (age < 21) and (money >= 5):
		return "You are not old enough to buy beer"
	else:
		return "You can't afford beer AND you're too young to purchase it"

print(beer(21,5))
print(beer(21,4))
print(beer(20,5))
print(beer(20,4))


#Lists - Have brackets []
movies = ["The Matrix", "Fight Club", "Inception", "Drive"]

print(movies[1]) #returns the second item in the list 
print(movies[0]) #returns the first item in the list
print(movies[1:3]) #returns the first number given until right before the last number
print(movies[1:4]) #returns all
print(movies[1:]) #returns everything from number to end of list
print(movies[:1]) #everything before 1
print(movies[:2]) 
print(movies[-1]) #grabs last itme

print(len(movies)) #counts items in list
movies.append("Spider-man")
print(movies) #appends to end of list

movies.insert(2, "Fargo")

movies.pop() #removes last item
print(movies)

movies.pop(0) #removes first item
print(movies)

#Looping

#For Loops - iterate start to finish
veggies = ["kale", "lettuce", "bell pepper"]
for x in veggies:
	print(x):

#While Loops - executes according to boolean statement
i = 1

while i < 10:
	print(i)
	i += 1

#Importing
import sys #system functions and parameters
from datetime import datetime as dt #import with alias

print(sys.version)
print(dt.now()) #.now is a method we can use


