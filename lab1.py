#metoda recursiva
def fib1(n):
    if n<2: 
        return n
    else:
        return fib1(n-1)+fib1(n-2)

#metoda iterativa
def fib2(n):
    i,j=1,0
    for k in range(n):
        j=i+j
        i=j-i
    return j

#metoda bazata pe multiplicare de matrici
def fib3(n):
    i,j,k,h=1,0,0,1
    while n>0:
        if n%2==1:
            t=j*h
            j=i*h+j*k+t
            i=i*k+t
        t=h*h
        h=2*k*h+t
        k=k*k+t
        n //= 2
    return j


for n in range(2,11):
    print(str(fib3(n))+" ")

