#number divisible by 7 and multiple of 5 between 1500 & 2700
for number in range(1500, 2701):
    if number % 7 == 0 and number % 5 == 0:
        print(number)







# Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))

f = (c * 9 / 5) + 32

print(c, "C is", f, "Fahrenheit")


# Fahrenheit to Celsius
f = float(input("Enter temperature in Fahrenheit: "))

c = (f - 32) * 5 / 9

print(f, "F is", c, "Celsius")







#guess number between 1 to 9
secret_number = 7

while True:
    guess = int(input("Guess a number between 1 and 9: "))

    if guess == secret_number:
        print("Well guessed!")
        break
    else:
        print("Wrong guess. Try again.")








#print stars pattern
# Increasing part
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Decreasing part
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()







#input word and reverse it 
word = input("Enter a word: ")

reverse_word = word[::-1]

print("Reverse:", reverse_word)







#count even and odd numbers 
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)










#print each item and its corresponding type 
datalist = [
    1452,
    11.23,
    1 + 2j,
    True,
    'w3resource',
    (0, -1),
    [5, 12],
    {"class": "V", "section": "A"}
]

for item in datalist:
    print("Item:", item)
    print("Type:", type(item))
    print()







#print numbers from 0 to 6 except 3 & 6
for number in range(7):
    if number == 3 or number == 6:
        continue

    print(number)








#fibonacci series between 0 and 50
a = 0
b = 1

while a <= 50:
    if a != 0:
        print(a, end=" ")
    
    next_number = a + b
    a = b
    b = next_number










#fizzBuzz
for number in range(1, 51):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)





#generate a 2D array
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

array = []

for i in range(rows):
    row = []

    for j in range(columns):
        row.append(i * j)

    array.append(row)

print(array)



 








#accept lines until blank line and convert to lowercase
print("Enter lines. Press Enter on a blank line to stop.")

while True:
    line = input()

    if line == "":
        break

    print(line.lower())






#find 4 digit binary number divisible by 5 
binary_numbers = input("Enter 4-digit binary numbers separated by commas: ")

numbers = binary_numbers.split(",")

result = []

for binary in numbers:
    decimal = int(binary, 2)

    if decimal % 5 == 0:
        result.append(binary)

print(",".join(result))











#count letter and digits in a string
text = input("Enter a string: ")

letters = 0
digits = 0

for character in text:

    if character.isalpha():
        letters += 1

    elif character.isdigit():
        digits += 1

print("Letters", letters)
print("Digits", digits)









#password validation 
import re

password = input("Enter your password: ")

if (6 <= len(password) <= 16
        and re.search(r"[a-z]", password)
        and re.search(r"[A-Z]", password)
        and re.search(r"[0-9]", password)
        and re.search(r"[$#@]", password)):

    print("Valid password")

else:
    print("Invalid password")
