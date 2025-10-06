def decor(fun): #r3
    def inner(): #r2
        value= fun() # r1
        return value+2
    return inner # r4


# @decor
def num():
    return 10

result_f=decor(num)
print(result_f())
