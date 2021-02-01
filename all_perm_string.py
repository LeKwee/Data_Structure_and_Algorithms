'''
print all permutation of a string
'''
def toString(List): 
    return ''.join(List) 

def all_perm_string(a, l, r):
    print(f'l: {l}, r: {r}')
    if l==r: 
        print (toString(a))
    else: 
        for i in range(l,r+1): 
            print(f'i, l, r: {i}, {l}, {r}')
            print(f'a[l], a[i]: {a[l]}, {a[i]}')
            a[l], a[i] = a[i], a[l] 
            all_perm_string(a, l+1, r) 
            a[l], a[i] = a[i], a[l]

if __name__ == '__main__':
    string = "ABC"
    n = len(string) 
    a = list(string) 
    all_perm_string(a, 0, n-1) 