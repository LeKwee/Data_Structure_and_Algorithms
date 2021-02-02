'''
Given an expression string, find whether a given string has balanced parentheses or not.
'''

def bal_parentheses(string):
    stack = []

    open_list = ['[','{','(']
    close_list = [']','}',')']
    
    for i in string:
        if i in open_list:
            stack.append(i)
        else:
            index = close_list.index(i)
            if len(stack)>0 and stack[-1]==open_list[index]:
                stack.pop()
            else:
                return 'Unbalanced'
    
    if len(stack)>0:
        return 'Unbalanced'
    return 'Balanced'

if __name__ == '__main__':
    string = "{[]{()}}"
    print(string,"-", bal_parentheses(string)) 
    
    string = "[{}{})(]"
    print(string,"-", bal_parentheses(string)) 
    
    string = "((()"
    print(string,"-",bal_parentheses(string)) 
