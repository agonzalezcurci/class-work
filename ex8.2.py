#  + concatenates lists 
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

# * repeats a given number of times 
q = [0] * 4
t = [1,2,3] * 3
print(t)
print(q)

#slice works on lists 
s = ['a','b', 'c', 'd', 'e', 'f']
print(s[1:3])
print(s[:4])
print(s[3:])
print(s[:])

# slice operator on left side an assignment can update multiple elements
s[1:3]= ["x","y"]
print(s)

# append method adds new element to list 
s.append('g')
print(s)

# extend appends all the elements in a list 
s1 = ["h","i", "j", "k" ]
s.extend(s1)
print(s)

# ways of deleting elements 

# if you know the index use pop method
x = s.pop(1)
print(s)
print(x)

#if you don't need the removed value use del operator 
del s[1]
print(s)

#if you know the element you want to remove but not the index use remove method
s.remove("a")
print(s)

# use slice and del to remove more than one element
del s[1:5]
print(s)

