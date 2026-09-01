# To be a DevOps engineer in my life we are going to learn about the python language.
# first we will learn about the basic syntex of python language or data types.
# First we will learn about the basic data tyepes list, tuple, set , dictionary,string,integer,float,boolean,complex.



a = [1,23,4,45,6,7,7] #This is a list created by using square brackets.
A = [2,5,6,7,8,9] #This is a list created by using square brackets.
print(a)
b = (1,3,4,5,6,7,7,3) #This is a tuple created by using round brackets.
print(b)
c ={9,8,9,5,5,7,2,5,8,1,3} #This is a set created by using curly brackets. IT will not allow duplicate values.
print(c)
d = {1:"One", 2:"Two", 3:"Three", 4:"Four"} #This is a dictionary created by using curly brackets. It will allow key values pair.
print(d)


# let's do the basic opreation on list, tuple, set, dictionary.

print(max(a))
print(min(a))
a.pop(4)
a.insert(4,1000)
print(a)

print(a+A)



print(max(b))

# tuple is a immutable data type. It means we can not change the value of the tuple once it is created.
# we can not add or remove any value from the tuple. It is a read only data type.


# set

c.add(111) # it will add the value in the set.


c.pop() # it will remove the first number of the set.
c.add(2000) # it will add the value in the set.

print(c)

#dictionary

d.keys() # it will return the keys of the dictionary.
d.values() # it will return the values of the dictionary.
d.pop(2) # it will remove the key value pair from the dictionary.
d["Honey Singh"] = "Munariya " # it will add the key value pair in the dictionary.   
print(d)