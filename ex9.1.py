# creates a dictionary which takes characters as keys and add their frequencies as values
word = 'brotosaurus'
d = dict()
for c in word:
	if c not in d:
		d[c] = 1
	else:
		d[c] = d[c] + 1
print(d)

#get method returns corresponding value for a key. 
# get can be used with the above histogram loop it automatically deals with keys not in dictionary 

word = 'brotosaurus'
d = dict()
for c in word:
	# get method takes key "c" and value 0 
	d[c] = d.get(c,0)+1
print(d)

