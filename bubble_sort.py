def bubble_sort(arr):
    print(f'Arr before sort: {arr}')
    swapping = True
    swap_count = 0

    while swapping:
        tmp = 0
        for i in range(len(arr)-1):
            if arr[i]> arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1]=tmp
                swap_count +=1
        if tmp == 0:
            swapping = False

    print(f'Arr after sort: {arr}')
    print(f'Number of swaps needed: {swap_count}')

if __name__ == '__main__':
    bubble_sort([1,2,3,6,5,7,8,4])