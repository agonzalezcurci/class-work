# guardian code to deal with blank lines 
fhand = open("mbox-short.txt")
for line in fhand:
	words = line.split()
	#this will act as guardian for blank lines
	if len(words) == 0: continue
	if words[0] != "From" : continue
	print(words[2])

#check to see what causes problem code
fhand = open("mbox-short.txt")
for line in fhand:
	words = line.split()
	#this will print the words which need debugging
	print('Debug:', words)
	if words[0] != "From" : continue
	print(words[2])
#problem code 
fhand = open("mbox-short.txt")
for line in fhand:
	words = line.split()
	if words[0] != "From" : continue
	print(words[2])
	
	

