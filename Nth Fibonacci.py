def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


n = int(input("Enter a number: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    print("Fibonacci number:", fibonacci(n))
