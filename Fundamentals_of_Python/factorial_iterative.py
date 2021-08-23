def factorial(n):
    if n < 0:
        return "Enter positive values"
    if n == 0 or n ==1:
        return 1

    counter= 1        
    for i in range(2, n+1):
        counter *= i
    return counter

print(factorial(6))
