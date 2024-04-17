def fib(n):
    f = []
    # Base cases: Fib(0) = 0, Fib(1) = 1
    for i in n:
        if i == 0:
            f[0] = 0
        elif i == 1:
            f[1] = 1
        f[i] = f[i-2] +f[i-1]

    return f[n]


n = 10
result = fib(n)
print("Fibonacci number at position " , n , ": " , result)