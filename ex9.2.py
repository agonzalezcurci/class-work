# nested loops can be used to break text into words 

fname = input("Enter the file name: ")
try:
 fhand = open(fname)
except: 
	print("File cannot be opened: ")
	exit()

counts = dict()
#outer loop
for line in fhand:
	words = line.split()
	#inner loop
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1
print(counts)
		
	
