def fib1(n):
    if n<2: 
        return n
    else:
        return fib1(n-1)+fib1(n-2)


for n in range(2,11):
    print(str(fib1(n))+" ")