# nput function

str =input("Enter input: ") #getting user input 
print("Received input is :",str)

#opening nd closing files
file=open("filename", "wb")
file.close() #closes an existing file

#reading and writing files
file.write("Python is great.\nYeah very great indeed\n") #writes to the file
str =file.read(10)