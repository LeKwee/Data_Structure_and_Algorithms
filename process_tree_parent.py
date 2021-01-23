def findParent(num):
    curr_max=1
    for i in range (1,num+1):
        for _ in range (i):
            start = max(curr_max, i)
            curr_max= start+1
            if curr_max == num:
                return i

def findParent_math(num):
    import math
    if num == 1:
        return None
    # num * (num+1)/2+1 ==  largest value belong to num parent
    parent = (math.sqrt((num-1)*2*4+1)-1)//2
    if num > (parent * (parent+1)/2)+1:
        return parent+1
    else:
        return parent

def testcase(num, ans):
    pred = findParent(num)
    assert pred == ans, f'Pred: {pred}, Correct Ans: {ans}'
    print("Test Successful!")

if __name__ == '__main__':
    '''
                1
                |          
                2
        |               |
        3               4
    |   |   |        |  |  |  |
    5   6   7        8  9  10 11
    |
    12...

    '''
    testcase(1,None)
    testcase(2,1)
    testcase(3,2)
    testcase(4,2)
    testcase(5,3)
    testcase(6,3)
    testcase(7,3)
    testcase(8,4)
    testcase(9,4)
    testcase(10,4)
    testcase(11,4)
    testcase(12,5)
    testcase(47,10)
    print(findParent(67))
    print(findParent_math(67))

