#quicker than 7.5
fhand = open('mbox-short.txt')
for line in fhand:
	#strips white space
	line = line.rstrip()
	#skips uninteresting lines
	if not line.startswith("From:"):
		continue
	#process interesting line
	print(line)