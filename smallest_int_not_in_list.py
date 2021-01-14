'''
Given an array of int between -1000000 to 1000000
return the smallest positive int that is not in array
'''

def get_smallest_missing_int(arr):
    if len(arr) == 0:
        return 1

    unique_arr = set(arr)
    curr = 0
    for i in range(1,len(unique_arr)+1):
        if i not in unique_arr:
            return i
        else:
            curr = i

    return curr+1

def testcase(arr, ans):
    pred = get_smallest_missing_int(arr)
    if pred != ans:
        print(f'Wrong ans: {pred}, Correct ans: {ans}, arr: {arr}')
    else:
        print(f'Correct! Arr: {arr}')

if __name__ == '__main__':
    testcase([], 1)
    testcase([0], 1)
    testcase([-1,-3], 1)
    testcase([1,2,3,4,5], 6)
    testcase([-2341,-232,-2343,-44,2345,234,1,2,3,4,63456,34533,-21352], 5)