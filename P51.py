def decor(fun):
    def inner():
        value= fun()
        return value+2
    return inner
# @ decor
def num():
    return 10
result_f=decor(num)
print(result_f())
