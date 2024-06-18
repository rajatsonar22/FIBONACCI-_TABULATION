# prcatical 11(b)
# FIBONACCI_TABULATION

print(">>>FIBONACCI_TABULATION")
print("")#...space

def fibonacci_tabulation(n):
    if n <= 1:
        return n
    else:
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range (2, n + 1):
            fib[i] = fib[i - 1] + fib [i - 2]
        return fib[n]

print("--- the required answer is:",fibonacci_tabulation(10))
