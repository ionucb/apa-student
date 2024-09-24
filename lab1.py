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
    global count_rec
    global count_it
    global count_mat
    ans=True
    while ans:
        print ("""
        1. fibonacci 10
        2. fibonacci 100
        3. fibonacci 1000
        4. fibonacci 10000
        5.Exit
        """)
        ans=input("What would you like to do? ") 
        if ans=="1": 
            fib1(10)
            fib2(10)
            fib3(10)
            print("recursiv:",count_rec)
            print("iterativ:",count_it)
            print("matrici:",count_mat)
        elif ans=="2":
            fib1(100)
            fib2(100)
            fib3(100)
            print("recursiv:",count_rec)
            print("iterativ:",count_it)
            print("matrici:",count_mat)
        elif ans=="3":
            fib1(1000)
            fib2(1000)
            fib3(1000)
            print("recursiv:",count_rec)
            print("iterativ:",count_it)
            print("matrici:",count_mat)
        elif ans=="4":
            fib1(10000)
            fib2(10000)
            fib3(10000)
            print("recursiv:",count_rec)
            print("iterativ:",count_it)
            print("matrici:",count_mat)
        elif ans=="5":
            print("\n Goodbye") 
        elif ans !="":
            print("\n Not Valid Choice Try again") 

if __name__ == "__main__":
    main()