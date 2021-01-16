'''
Given two strings, determine if they share a common substring. A substring may be as small as one character.

Returns: "YES" or "NO"
'''

def twoStrings(s1,s2):
    # check if any char in one string is in another string
    # for fast look up, use dict

    in_s1 = dict(zip(list(s1), range(len(s1))))

    for char in s2:
        if char in in_s1:
            return "YES"
    return "NO"

def testcase(s1,s2,ans):
    if ans == 'YES':
        output = 'Substring exist but returned "NO"'
    else:
        output = 'Substring does NOT exist but returned "YES"'
    assert twoStrings(s1,s2) == ans, output 
    print('TEST CASE PASSED')

if __name__ == '__main__':
    testcase('hello', 'world', 'YES')
    testcase('hi', 'world', 'NO')