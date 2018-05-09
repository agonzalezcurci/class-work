
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
	line = line.translate(line.maketrans(" ", " ", string.punctuation))
	line = line.lower()
	words = line.split()
	for word in words:
		letter = word.split()
		for letter in word:
			if letter not in counts:
				counts[letter] = 1
			else: 
				counts[letter] += 1
l = list()
for key, val in list(counts.items()):
	l.append((val, key))

l.sort(reverse=True)

for key, val in l:
	print(key,val)