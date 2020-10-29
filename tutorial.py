print ("Hello world!!!") # prints to console.

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
friends.clear() #clears everything from the list
friends.pop() #removes last element
friends.index("Kevin") #says if kevin is in the list, if name isnt in list, it produces an error






