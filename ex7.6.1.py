# elegant or pythonic way to insure no error if someone does not type in a file name
fname = input("Enter file name")
try:
	fhand = open(fname)
except:
	print("This File Cannot be Opened: ", fname)
	exit()
count = 0
for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1
print("There were", count, "subject lines in", fname)
