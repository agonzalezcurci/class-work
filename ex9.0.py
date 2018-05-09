#dictionaries are a map between two indices called a key-value pair 
eng2sp = {"one": "uno", "two": "dos", "three": "tres"}
print(eng2sp) 

# dictionary key lets you look up attached value 
print(eng2sp["two"])
 
# len returns the number of pairs 
print(len(eng2sp))

# in operator tell us if key in dictionary 
if "one" in eng2sp: 
	print("True")
else: 
	print("False")
if "uno" in eng2sp:
	print("True")
else: 
	print("False")	

#use method values to turn values into a list to see if a value is in a dictionary 
vals = list(eng2sp.values())
if "uno" in vals:
	print("True")
else: 
	print("False")
