# most common words 
# first part reads file and computes dictionary that maps each word to count in documents see 9.4 

import string 

fname = input("Enter the file: ")
try:
	fhand = open(fname)
except:
	print("File cannot be opened: ", fname)
	exit()

counts = dict()
for line in fhand:
	line = line.rstrip()
	# translate deletes punctuation
	line = line.translate(line.maketrans(" ", " ", string.punctuation))
	line = line.lower()
	words = line.split()
	for word in words:
		if word not in counts:
			counts[word] = 1
		else: 
			counts[word] += 1
			
#sort the dictionary by value 
l = list()
for key, val in list(counts.items()):
	l.append((val, key))
#sort by reverser order
l.sort(reverse=True)

#loop to print ten most common words 
for key, val in l[:10]:
	print(key,val)