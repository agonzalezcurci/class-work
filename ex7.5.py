fhand = open('mbox-short.txt')
for line in fhand:
	#strips white space
	line = line.rstrip()
	#only prints lines that start with "From"
	if line.startswith("From:"):
		print(line)