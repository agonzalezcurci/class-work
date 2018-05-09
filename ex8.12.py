# a and b are aliased meaning the are referenced together 
a = [1,2,3,4]
a = b
print(b[0])

# changes made in one affect the other 
b = [17,2,3,4]
print(a)