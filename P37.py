def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
if __name__ == "__main__":
    num = 6
    print(f"Factorial of {num} is {fact(num)}")