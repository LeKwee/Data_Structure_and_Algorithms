'''
A box contains n number of chocolates.
1 or 3 chocoloates can be removed at a time.
How manys ways can the box be emptied?

eg: 7 chocolates in a box
(3,3,1)
(3,1,3)
(1,3,3)
(1,1,1,1,3)
(1,3,1,1,1)
(1,1,3,1,1)
(1,1,1,3,1)
(3,1,1,1,1)
(1,1,1,1,1,1,1)
================
Total: 9 ways
'''

import time
counts = {
        'count_removeChoc': 0,
        'count_removeChoc_OPTIMISED':0
        }

def removeChoc(n):
    counts['count_removeChoc']+=1
    if n == 3:
        return 2
    if n == 1:
        return 1
    if n < 0:
        return 0
    return removeChoc(n-1) + removeChoc(n-3)

def removeChoc_OPTIMISED(n, seen=None):
    counts['count_removeChoc_OPTIMISED']+=1
    if seen == None:
        seen={}

    if n in seen:
        return seen[n]
    if n == 3:
        return 2
    if n == 1:
        return 1
    if n < 0:
        return 0
    ret = removeChoc_OPTIMISED(n-3, seen) + removeChoc_OPTIMISED(n-1, seen)
    seen[n] = ret
    return ret


def testcase(n_choc, correct_ans, func):
    ret = func(n_choc)
    assert ret == correct_ans, f"FAILED {func}: Choc={n_choc}, Returned: {ret}, Correct_ans: {correct_ans} "
    print(f'TEST {func}, Choc={n_choc} passed.')

if __name__ == "__main__":
    testcase(7,9, removeChoc)
    testcase(7,9, removeChoc_OPTIMISED)

    start_time = time.time()
    removeChoc(50)
    time_took = time.time() - start_time
    print(f'removeChoc time: {time_took}')
    print(f"Recursion count: {counts['count_removeChoc']}")

    start_time = time.time()
    removeChoc_OPTIMISED(50)
    time_took = time.time() - start_time
    print(f'removeChoc_OPTIMISED time: {time_took}')
    print(f"Recursion count: {counts['count_removeChoc_OPTIMISED']}")

"""
RESULTS:

TEST <function removeChoc at 0x000001EFDEFD7280>, Choc=7 passed.
TEST <function removeChoc_OPTIMISED at 0x000001EFDEFD7310>, Choc=7 passed.
removeChoc time: 63.1922550201416
Recursion count: 202751530
removeChoc_OPTIMISED time: 0.0
Recursion count: 108
"""