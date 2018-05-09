fhand = open(filename)
for line in fhand:
	words = line.split()
	if len(words) == 0: continue
	if words[0] != "From" : continue
print(words[1])