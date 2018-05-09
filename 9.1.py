fhand = open("data/words.txt")
keys = dict()
for lines in fhand:
	words = lines.split()
	for word in words:
		if word not in keys:
			keys[word] = 1
		else: 
			keys[word] += 1
print(keys)
		



