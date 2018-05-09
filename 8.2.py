filename = input("please type file name: ")
try:
	fhand = open(filename)
	for line in fhand:
		words = line.split()
		#this will act as guardian for blank lines
		if len(words) == 0: continue
		if words[0] != "From" : continue
		print(words[2])
except: 
	print("This file does not exist in this directory")	