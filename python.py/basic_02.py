# In this file we will learn about some more advance concept of python language.
# if else, elif, for loop, while loop, break, continue, pass, function, class, object, inheritance, polymorphism, encapsulation, abstraction.

# Conditional operators: 

# if else statement

# == - Equal To
# != - not equal to
# > - Greater than
# < - Less than
# >= - Greater than or equal to
# <= - Less than or equal 

age= int(input("Enter your age\n "))

if age >= 18:
    print("You are eligible to vote")
elif age < 18 and age >= 0:
    print("You can not give the vote")
else:
    print("Invalid age")

# for loop:

a = [1,2,3,4,5,6,7,8,9]

for i in a:
    print("Honey singh munariya")
    print(i)

# range method
for i in range(1,11):
    print("Honey singh")
    print(i)


# modules

# we can import the modules in python by using import keywords
# we can even create our own modules in python by creating a python file and then importing it in another python file.

from basic import rest
print(rest.banana)
print(rest.apple)
print(rest.orange)
print(rest.graps)