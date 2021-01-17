'''
Given an unordered array of consecutive int without any duplicates.
Find minimum number of swaps required to sort array in ascending order.
'''

def min_swap(arr):
    # zip arr numbers to index representing the correct sequece
    # check from position 1 to len(arr), if they are not in the correct position, swap it with the correct position.

    tracker = dict(zip(arr, range(1,len(arr)+1)))

    swap_count=0
    # lopp from 1 to last number
    for i in range(1, len(arr)+1):
        # if number not in the right position
        if tracker[i] != i :
            # swap whatever number was in curr number's supposed position to curr number's curr position.
            arr[tracker[i]-1] = arr[i-1]
            # update tracker
            tracker[arr[i-1]] = tracker[i]
            swap_count +=1

    return swap_count