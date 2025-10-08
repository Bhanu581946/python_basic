def add(farg,*args):
    print("Formal argument=", farg)
    sum=0
    for i in args: # i=10, 20, 30
        sum += i   # sum=0+10=10, 10+20=30, 30+30=60
    print("sum of all numbers",(farg+sum)) #65
add(5,10)
add(5,10,20,30)