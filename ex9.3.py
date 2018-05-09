counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
	print(key, counts[key])

# only retrieves is value is higher than ten
for key in counts:
	if counts[key] > 10:
		print(key, counts[key])

# sorts by key a-z
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
	print(key, counts[key])
	