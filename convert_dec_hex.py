'''
hex: 1 2 3 4 5 6 7 8 9  A   B   C   D   E   F
dec: 1 2 3 4 5 6 7 8 9  10  11  12  13  14  15

hex --> dec
C9 = 12*(16^1) + 9*(16^0) = 201

dec --> hex
                        remainder
201 // 16 = 12      |       9
12 // 16 = 0        |       12
                           ----
                            C9
'''

def dec_to_hex(dec):
    
    quo = -1
    remainder = []
    while quo != 0 :
        quo = dec//16
        remainder.append(dec%16)
        dec = quo

    mapping = {
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F'
    }

    ret = ''
    for i in range(len(remainder)-1,-1,-1):
        if remainder[i] <10:
            ret+=str(remainder[i])
        else:
            ret+=mapping[remainder[i]]
    
    return ret

if __name__ == '__main__':
    print(dec_to_hex(201))
            