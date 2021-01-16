'''
Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is "NO.

Input: list of strings for each word in mag and another list for each word in ransom note
Return: print "yes" or "no"
'''

def ransomNote(mag, note):
    mag_words = {}
    for word in mag:
        if word in mag_words:
            mag_words[word]+=1
        else:
            mag_words[word] = 1

    for word in note:
        if word in mag_words and mag_words[word]>0:
            mag_words[word] -=1
        else:
            return("no")
    return('yes')

def testcase(mag,note,ans):
    assert ransomNote(mag,note) == ans, "Wrong ans!"
    print('TEST CASE PASSED')

if __name__ == '__main__':
    mag = ['What','a','good','day','to','have','pot','luck']
    note1 = ['good', 'luck']
    note2 = ['Good', 'luck']

    testcase(mag,note1,'yes')
    testcase(mag,note2,'no')