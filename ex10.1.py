# tuples
t1 = ("a",)
print(type(t1))

#string 
t2 = ("a")
print(type(t2))

# built in tuples
t = tuple()
print(t)

# if argument is a sequence the result of tuple is elements 
t = tuple("lupins")
print(t)

# list operators work on tuples 
print(t[0])
 
print(t[1:3])
 
 #You cannot add to a tuple, but you can replace one tuple with another 
t = ("L",) + t[1:]
print(t)

