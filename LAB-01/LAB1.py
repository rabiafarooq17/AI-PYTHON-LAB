print("MY NAME IS RABIA") #this is first ai lab

name=input("TYPE YOUR NAME: ")
print(name)
age=input("YOUR AGE:")
print(age)
height=input("Your height:")

print("I AM A CS STUDENT")
print("I am good in coding")
#we can print above two statements on same line by putting a semicolon between them
print("I AM A CS STUDENT") ; print("I am good in coding ")
 
#NOW WE ARE MOVING TOWARDS INDENTATION AND TAB
x=1
if x>0:
 print("I am using python") #this is single space
    
print(type(name))
print(type(age))
print(type(height)) # IT SHOWAS ALL THREE TYPES AS STR BCZ INPUT ALWAYS SHOWS TXT BUT IF I WRITE int(input(age))then it will show as int datatype viceversa to float as we put it before input in height

#here we define the complex data type
x = 2 + 3j
print(x)
print(type(x))

print("my name is \"RABIA\"")

string1="PYTHON"
print(string1[0]) #string indexing
print(string1[3]) #out of range

#now we are going to learn about list
my_list1=[1,3,5,7]                         #list contains integers
print()
my_list2=['red','blue','green','pink']     #list contains sring
my_list3=['red',1,2.3]                     #list contains int,str,float

fruits = ["Apple", "Banana", "Mango", "Orange"] #list indices
print(fruits[-1])
print(fruits[2])

#list slicing
print(fruits[1:3])
print(fruits[-4:-1])


