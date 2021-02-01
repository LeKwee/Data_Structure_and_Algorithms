'''
Given 2 sorted array, merge them in sorted manner
'''

def merge_arr(arr1, arr2):
    len1 = len(arr1)
    len2 =  len(arr2)
    i,j = 0,0
    arr = []

    while i < len1 and j < len2:
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1

    while i < len1:
        arr.append(arr1[i])
        i+=1

    while j < len2:
        arr.append(arr2[j])
        j+=1
        
    return arr

if __name__ == '__main__':
    arr1 = [1,3,5,7]
    arr2 = [2,4,6,8]

    print(merge_arr(arr1,arr2))