'''
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset. It is possible that the maximum sum is 0, the case when all elements are negative.

For example, given an array [-2,1,3,-4,5] we have the following possible subsets. These exclude the empty subset and single element subsets which are also valid.

[-2,3,5] = 6
[-2,3]   = 1
...
...
[3,5]    = 8

return 8
'''

def max_arr_sum(arr):
    # keep track of largest possible combination at each index.
    # every next index after index 2,
    # check max(nex index, current largest combi, new index + new index-2)

    if len(arr) == 1:
        return arr[-1]

    tracker = []
    tracker.append(arr[0])
    tracker.append(max(arr[0],arr[1]))

    for i in range(2,len(arr)):
        tracker.append(max(tracker[-1], arr[i], arr[i]+tracker[-2]))
    return tracker[-1]

def testcase(arr, ans):
    pred = max_arr_sum(arr)
    assert pred == ans, f'Predicted: {pred}, Correct Ans: {ans}'
    print('TEST CASE SUCCESS!')

if __name__ == '__main__':
    arr = [2,1,5,8,4]
    testcase(arr, 11)