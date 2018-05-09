#write a file 
fout = open("output.txt", 'w')
print(fout)

#add line 
line1 = "This here is the wattle, \n"
fout.write(line1)

#add second line 
line2 = "emblem of our land. \n"
fout.write(line2)

#closes file
fout.close()
