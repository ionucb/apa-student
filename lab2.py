import time
import random

# Mergesort Implementation
def merge(left, right):
    result = []
    i = j = 0

    # Combinăm cele două liste ordonate
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Adăugăm elementele rămase din fiecare listă
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    # Împărțim lista în două părți
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    # Interclasăm cele două liste
    return merge(left, right)

# Quicksort Implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    # Alegem pivotul ca primul element din listă
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    # Apelăm recursiv pentru sublistele mai mici și mai mari decât pivotul
    return quicksort(less) + [pivot] + quicksort(greater)

# Funcția de analiză empirică
def analyze_sorting_algorithms():
    sizes = [100, 1000, 5000, 10000, 50000, 100000]  # Dimensiuni ale tablourilor de test
    for size in sizes:
        # Generăm un tablou aleatoriu de dimensiunea dată
        arr = [random.randint(1, 100000) for _ in range(size)]
        
        # Măsurăm timpul pentru Mergesort
        start_time = time.time()
        mergesort(arr.copy())  # Folosim o copie pentru a nu modifica lista inițială
        mergesort_time = time.time() - start_time
        
        # Măsurăm timpul pentru Quicksort
        start_time = time.time()
        quicksort(arr.copy())
        quicksort_time = time.time() - start_time
        
        print(f"Array size: {size}")
        print(f"Mergesort time: {mergesort_time:.6f} seconds")
        print(f"Quicksort time: {quicksort_time:.6f} seconds")
        print('-' * 40)

# Funcția principală
def main():
    print("Empirical analysis of sorting algorithms:\n")
    analyze_sorting_algorithms()

if __name__ == "__main__":
    main()
