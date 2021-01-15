'''
Given a string, return the longest palindromic substring 
Example:
'daddffddgthtg'
return: 'ddffdd'
'''

def get_longest_palin(s):
    res=''
    for index in range(len(s)):
        ret = __find_longest_palin(index,index,s)
        res = max(res,ret,key=len)
        ret = __find_longest_palin(index, index+1,s)
        res = max(res,ret,key=len)
    return res

def __find_longest_palin(left,right,s):
    while left>=0 and right<len(s) and s[left] == s[right]:
        left-=1
        right+=1
    
    return s[left+1:right]

def testcase(s, ans):
    pred = get_longest_palin(s)
    assert pred == ans, f"Your ans: {pred}, Correct ans: {ans}"
    print('Test Successful')

if __name__ == '__main__':
    testcase('daddffddgthtg', 'ddffdd')
    testcase('daddfddghtg', 'ddfdd')
