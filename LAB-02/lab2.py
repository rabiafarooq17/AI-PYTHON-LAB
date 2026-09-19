#python program to illustrate
#while loop

count=0
while (count<3):
       count=count+1
       print("Hello Geek")

# Single statement while block
count = 0
while (count == 0): print("Hello Geek")

Example 1
# Python program to illustrate
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
   print(i)

Example 2
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
  print(i)

Example 3
# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s :
  print(i)

# Python program to illustrate
# Iterating by index
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
   print list[index]

# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
if letter == 'e' or letter == 's':
   continue
print 'Current Letter :', letter
var = 10

# break the loop as soon it sees 'e'
# or 's'
if letter == 'e' or letter == 's':
break
print 'Current Letter :', letter

def my_function():
print("Hello from a function")

def my_function():
print("Hello from a function")
my_function()

def my_function(fname):
print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

my_function(country ="Norway"): print("I am from "+ country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
for x in food:
print(x)
fruits = ["apple", "banana", "cherry"] my_function(fruits)

def my_function(x):
return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

def my_function(child3, child2, child1):
print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

class Person:
def init (self, name, age): self.name = name
self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

class Person:
def init (self, name, age): self.name = name
self.age = age
def myfunc(self):
print("Hello my name is " + self.name)
p1 = Person("John", 36) p1.myfunc()

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = key

    return arr


numbers = [5, 2, 4, 6, 1, 3]

print("Before sorting:", numbers)

insertion_sort(numbers)

print("After sorting:", numbers)
