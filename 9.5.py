filename = input("please type file name: ")
try:
	fhand = open(filename)
	count = dict()
	for line in fhand:
		words = line.split()
		if not len(words) == 0 and words[0] == "From" : 
			start = words[1].find("@")
			domain = words[1] [start+1:]
			if word not in count:
				count[domain]= 1
			else: 
				count[domain]+= 1
	print(count) 
				
except: 
	print("This file does not exist in this directory")

	
	