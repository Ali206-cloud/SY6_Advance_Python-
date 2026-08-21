n = int(input("Enter your number:"))
array = [0]*(n+1)


if n >= 1:
    array[1] = 1
for i in range(2, n + 1):
    array[i] = array[i - 1] + array[i - 2]
print("Your Fibonacci number:", array[n])
print("Array:", array)      
