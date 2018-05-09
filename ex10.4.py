#Dictionaries have item method which returns a list of tuples which can now be sorted by key

d = {"b":10, "a":1, "c": 22}
t = list(d.items())
print(t)
t.sort()
print(t)

# combining items, tuple assignments and for, you get a code which traverses the key and values in a dict in a single loop 
for key, val in list(d.items()):
	print(val, key)

# same technique used to sort by value 
l = list()
for key, val in d.items():
	l.append((val, key))
print(l)

l.sort(reverse=True)
print(l)


	

