import time

count_rec=0
count_mat=0
count_it=0

#metoda recursiva
def fib_rec(n):
    global count_rec
    if n<2: 
        count_rec+=1
        return n
    else:
        count_rec+=1
        return fib_rec(n-1)+fib_rec(n-2)

#metoda iterativa
def fib_it(n):
    global count_it
    count_it,i,j=0,1,0
    for k in range(n):
        j=i+j
        i=j-i
        count_it+=1
    return j

#metoda bazata pe multiplicare de matrici
def fib_mat(n):
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

def menu(n):
    print("\nSelect the algorithm.")
    print("1. Recursive.")
    print("2. Iterative.")
    print("3. Matrix exponentiatio.")
    print("0. Exit")

    choice = input("Please select an option: ")

    if choice == '1':
        print("\n----------------- RECURSIVE -----------------")
        start_time = time.time()
        print("fibonacci number is:",fib_rec(n))
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'{count_rec} schimbări au avut loc în {execution_time:.4f} secunde.')

    elif choice == '2':
        print("\n----------------- ITERATIVE -----------------")
        start_time = time.time()
        print("fibonacci number is:",fib_it(n))
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'{count_it} schimbări au avut loc în {execution_time:.4f} secunde.')

    elif choice == '3':
        print("\n----------------- MATRIX -----------------")
        start_time = time.time()
        print("fibonacci number is:",fib_mat(n))
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'{count_mat} schimbări au avut loc în {execution_time:.4f} secunde.')

    elif choice == '0':
        exit()

    else:
        print("Invalid choise. Please select another option...")
        menu(n)
        

def main():
    n=int(input("which fibonacci number do you want to know?\n> "))
    while True:
        menu(n)



if __name__ == "__main__":
    main()