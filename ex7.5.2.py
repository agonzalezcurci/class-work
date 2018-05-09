#finds where string is in line using finds
fhand = open('mbox-short.txt')
for line in fhand:
	#strips white space
	line = line.rstrip()
	#only prints out line with found string
	if line.find("@uct.ac.za") == -1: 
		continue
	print(line)