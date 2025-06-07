def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = input("Number:")
num=num.strip()

if not num.isdigit():
    print("dne.")
else:
    num = int(num)
    if num < 0:
        print("dne")
    else:
        print(factorial(num))
