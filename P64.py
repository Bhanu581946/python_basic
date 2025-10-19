f= open("myfile","w")
a,b=[int(x) for x in input ("Enter two nmbers").split()]
c=a/b
f.write("writing %d into myfile"%c)
f.close()
print('File closed')