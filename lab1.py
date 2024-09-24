count_rec=0
count_mat=0
count_it=0

#metoda recursiva
def fib1(n):
    global count_rec
    if n<2: 
        count_rec+=1
        return n
    else:
        count_rec+=1
        return fib1(n-1)+fib1(n-2)

#metoda iterativa
def fib2(n):
    global count_it
    count_it,i,j=0,1,0
    for k in range(n):
        j=i+j
        i=j-i
        count_it+=1
    return j

#metoda bazata pe multiplicare de matrici
def fib3(n):
    global count_mat
    i,j,k,h=1,0,0,1
    while n>0:
        count_mat+=1
        if n%2==1:
            t=j*h
            j=i*h+j*k+t
            i=i*k+t
        t=h*h
        h=2*k*h+t
        k=k*k+t
        n //= 2
    return j

def main():
    fib1(1)
    print("recursiva:",count_rec)
    fib2(5)
    print("iterativa:",count_it)
    fib3(5)
    print("multiplicarea de matrici:",count_mat)

if __name__ == "__main__":
    main()