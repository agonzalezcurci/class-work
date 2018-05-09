filename = input("please type file name: ")
try:
	fhand = open(filename)
	count = dict()
	for line in fhand:
		words = line.split()
		if not len(words) == 0 and words[0] == 'From': 
			end = words[5].find(":")
			domain = words[5] [:end]
			if domain not in count:
				count[domain]= 1
			else: 
				count[domain]+= 1
	l = list(count.items())

	l.sort()
	
	for item in l:
		print(item)
	
except: 
	print("This file does not exist in this directory")
	
