try:
    f=open("myfile", "w")
    a,b= [int(x) for x in input("enter two nos").split()]
    c=a/b 
    f.write("writing %d into my file" %c)
except ZeroDivisionError:
    print("division by zero")
    print("please do not enter 0 in input")
finally:
    f.close()
    print("file closed")