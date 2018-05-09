# can covert string into list of characters using list
s = "spam"
t = list(s)
print(t)

# can break string into words using split method
s = 'pining for the fjords'
t = s.split()
print(t)
print(t[3])

# use split to space out delimiters 
s = 'spam-spam-spam'
delimiter = '-'
print(s.split(delimiter))
