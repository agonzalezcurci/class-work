# t acts as an allias for letters 
def delete_head(t):
	del t[0]

letters = ['a','b','c']
delete_head(letters)
print(letters)

# if you want to modify a list using a function makes sure the the method used does not create a new list

# slice operator creates a new list, and so function cannot work with an alias 

# instead write a function that returns a new list instead

def tail(t):
	return t[1:]

rest = tail(letters)
print(rest)


