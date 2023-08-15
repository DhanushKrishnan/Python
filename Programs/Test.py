"""
number = 9952866481
number_str = "9952866481"
name = "Dhanush"
print(type(number_str))
number_str = int(number_str)
print(name,number,number_str)
print(type(number_str))
name = input('Enter your name:')
print("Your name is:",name)
age = input('Enter your age:')
print("Your age is:",age)
number1 = float(input('Enter the number-1:'))
number2 = float(input('Enter the number-2:'))
number3 = float(input('Enter the number-3:'))
if number1 > number2: #& number1 > number3:
    print("Number 1 is greater than Number 2 and 3")
elif number2 > number1: #& number2 > number3:
    print("Number 3 is greater than Number 1 and 2")
else:
    print("Number 2 is greater than Number 1 and 3")
"""
"""for i in range(1,51,5):
    print("Dhanush",i)
for i in 'string':
    print(i)"""
"""i=1
while i < 51 :
    print(i)
    i+=1"""

"""fruits = [
    'apple',
    'mango',
    'pineapple',
    'banana'
]
print(fruits)
print(fruits[::-1])
fruits[0] = 'berry'
print(fruits)
length = len(fruits)
print(length)
fruits.append('papaya')
print(fruits)
TF = 'pineapple' in fruits
print(TF)
fruits.pop(2)
print("Not sorted:",fruits)
fruits.sort()
print("Sorted in alphabet order:",fruits)"""

"""def printing_function(string):
    for char in string:
        print(char)
printing_function('Dhanush')"""

def function(string):
    return string[::-1]
reversedString = function('Dhanush')
print("Reversed:",reversedString)