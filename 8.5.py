filename = input("please type file name: ")
try:
	fhand = open(filename)
	count = 0
	for line in fhand:
		words = line.split()
		if len(words) == 0: continue
		if words[0] != "From" : continue
		count = count + 1
		print(words[1])
	print("there are ", count,"line in the file with From as the first word")
except: 
	print("This file does not exist in this directory")	 

