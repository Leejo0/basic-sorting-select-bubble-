def selectionsort(A,n):
    if(n>1):
        k = findlargest(A,n-1)
        A[n-1],A[k] = A[k],A[n-1]
        selectionsort(A,n-1)

def findlargest(A,last):
    largest = 0
    for i in range(last):
        if(A[i] > A[largest]):
            largest = i
    return largest

def bubblesort(A,n):
    for i in range(n-1):
        if(A[i]>A[i+1]):
            A[i],A[i+1] = A[i+1],A[i]
    if n>1:
        bubblesort(A,n-1)

def bubblesortfast(A):
    n = len(A)
    for num in range(n,0,-1):
        swapped = False
        for i in range(num-1):
            if A[i] > A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
                swapped = True
        if not swapped:
            break


A = [10,4,19,2,1]
selectionsort(A,len(A))
print(A)
