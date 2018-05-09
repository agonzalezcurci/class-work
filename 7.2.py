fname = input("Enter file name \n")
try:
	fhand = open(fname)
except:
	print("This File Cannot be Opened: ", fname)
	exit()
count = 0
sum = 0	
for line in fhand:
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	atpos = line.find(" ")
	sppos = line.find("'\'",atpos)
	host = line[atpos+1:sppos]
	number = float(host)
	count = count + 1
	sum = sum + number
average = sum/count
print("Average Spam Confidence is:", average)