# Type 1 here we call fun inside display so that it can return a value
# def display(fun):
#     return "hi"+ fun()  

# def message():
#     return 'How are you'

# print(display(message))




# Type 2 , here we just write the reference of message i.e name which is fun and call message inside display
def display(fun):
    return "hi"+ fun  

def message():
    return 'How are you'

print(display(message()))

