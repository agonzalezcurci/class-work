filename = input("please type file name: ")
try:
	fhand = open(filename)
	count = dict()
	for line in fhand:
		words = line.split()
		if len(words) == 0: continue
		if words[0] != "From" : continue
		if words[1] not in count:
			count[words[1]] = 1
		else: 
			count[words[1]] += 1
	print(count) 
				
except: 
	print("This file does not exist in this directory")	