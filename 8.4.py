fhand = open("data/romeo.txt")
solos = []
for line in fhand:
	words = line.split()
	for x in words:
		if x in solos: continue
		solos.append(x)
solos.sort()
print(solos)

