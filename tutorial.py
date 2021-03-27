print ("Hello world!!!") # prints to console.
import time; #imports the time module

#variables 
char_name = "Alpha"
char_age = "38"

#using variables/concatenation 
print("My name is "+char_name+ " and am "+char_age+" years old.")

#changing variable value
char_name = "Emmanuel"
print(char_name)

#data types --> Strings ,numbers, decimals,boolean
#string functions
phrase = "Girrafe Academy"
print(phrase.upper()) #converts to uppercase
print(phrase.isupper()) #return true or false
print(len(phrase)) #returns length of stringprint 
print(phrase[0]) #returns the char at specified index
print(phrase.index("G")) #returns index of specified char...can also be used with words
print(phrase.replace("Girrafe","Elephant")) #replaces first with second

from math import * #imports math module

#get input from user;
#input("Enter your name") #alerts user to enter name ...

#name = input("Enter your name: ") #use the python terminal
#print("Hello "+name)

# lists in python--- samea as array

friends = ["Kevin","David","Lucky","Night",True,False]
luck_nums  = [23,23,2,2,4,]
print(friends[1]) #prints kevin
print(friends[-1]) #starts counting from back so prints 46
print(friends[1:]) #prints everything after kevin
friends.extend(luck_nums) #appends luck_num to friends
print(friends)

friends.append("Creed") #adds to the end
friends.insert(1, "John") # adds john at index 1
friends.remove("Lucky") 
#friends.clear() #clears everything from the list
#friends.pop() #removes last element
#friends.index("Kevin") #says if kevin is in the list, if name isnt in list, it produces an error
#friends.count("Kevin") #specifies how may times kevin is in the list
#friends.sort() #sorts alphabetically
#friends.reverse() #reverses friends order

friends_2 = friends.copy() #copies friends to friends_2

##tuples ---similar to lists ..they cant bemodified whatssoever
coodinates = (4,5,4) #cretes a tupple

###FUNCTIONS 
def sayhi(person, age):
	print("Hello "+person+" you are "+ str(age)) #indentation is very important;

sayhi("Mike",45); ##calls the function.....

def cube(num):
	return num*num*num #return statement...this can be stored

result = cube(45) #holds the value of calling the cube function
print(result)

####IF STATEMENTS
is_male = True
is_tall = False

if is_male or is_tall: #or keyword executes when one or both is true ..and keyword is also used
	print("You are male or tall or both.")
else:
	print("You are not male") # if not(is_male) --->negates the is_male value

###DICTIONARIES --correspond to objects ..store values in key value pair

conversion = {
	"jan":"January", #all keys have to be unique
	"feb":"February",
	"mar":"march"
}

print(conversion["jan"]) #gets the value associated with key
print(conversion.get("feb")) #gets value too
print(conversion.get("sept","Invalid month")) #prints out second arguement if first isnt in the dictionary


###WHILE LOOPS 
interger = 1
while interger<=10: ## this will execute as long as integer is less than 10
	print(interger) #is int <= 10? if yess, print the int
	interger +=2 #after printing the int, increment it by 1
	
###FOR LOOPS

for letter in "Girrafe Academy":
	print(letter) ##prints out every char in the girrafe academy

persons = ["Tim","Wilm","Jim"]

for person in persons:
	print(person)

for num in range(10): #range(3,10)--prints from 3 to 9
	print(num)

###Catching errors

try:
	value = 10/0
	number = int(input("Enter a number"))
	print(number)
except ZeroDivisionError: #handles the first error 
	print("Divided by zero")
except ValueError:
	print("Invalid input")

####dealing with files...
myfile = open("filename","r") #r is for reading ...you can use "w" for writing, "a" is append, "r+" read and write access
print(myfile.readable()) #returns true or false depending on files readability
print(myfile.read()) #prints out entire file
print(myfile.readline()) #prints out file lines and moves to next line
print(myfile.readlines()) #takes each line and puts it in an array..

myfile.close() #closes a file 

###MODULES...
import file  ##google "list of python modules"
##pip is a package manager...
##open the cmd

#date and time

localtime= time.localtime(time.time())

#python functions
def sayHi(name):
	print ("Hello",name)

sayHi("Alpha")

#referencing vs value
def changeValue(arr):
	arr.append([1,3,3,2,4])
	return

arr=[12,23,12,43,4,43,34,4,34]
changeValue(arr)
print (arr)

#keyword arguments
def printMe(str):
	print (str)
	return

printMe(str="My name is Alpha")

def info(name, age):
	print ("Name:", name)
	print ("Age:", age)
	return;

info(age=50, name="Alpha") #order doesnt matter with keyword arguments

#default aurguments

def agename(name,age=35):
	print ("Name:",name)
	print ("Age:",age)
	return;

agename(name="Alpha")  #prints both age and name...age will have the default value

#variable length arguments

def printInfo(arg1, *vartuple): #* used for var length args, when you arent sure how many args you will need;
	print("Output is", arg1)
	for var in vartuple:
		print (var)
	return;

printInfo("Hello",10,45,"rest")

#anonymous functions
add = lambda arg1,arg2: arg2+arg1;

print ("Value sum is",add(10,20));



