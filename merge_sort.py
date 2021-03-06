def merge_sort(arr):
    if len(arr)==1:
        return arr
    
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]

    merge_sort(L)
    merge_sort(R)

    i,j,k = 0,0,0

    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1

    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1

    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1

if __name__ == '__main__':
    arr = [43,21,734,21,23,4,2,1,9]

    merge_sort(arr)

    print(arr)