def decorator(f):
    def wrapper():
        print("Something is happening before the function is called.")
        f()
        print("Something is happening after the function is called.")
    return wrapper
@decorator
def greet():
    print("Hello, World!")
greet()