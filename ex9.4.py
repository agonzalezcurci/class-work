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
print(counts)
		
	