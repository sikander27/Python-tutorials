#test.py

'''
write a function which reverse the given string without changing position of special characters like [@,#,$,%,^]
eg: reverse_me = "Int@Fin^eg#"
o/p : "gen@iFt^nI#"
'''
def reverse_me(s):
    sp_char = ['@','#','$','%','^']
    new_string = []
    my_index = {}
    for i in range(len(s)):
        if s[i] in sp_char:
            my_index[s[i]] = i
        else:
            new_string.append(s[i])
    res = new_string[::-1]
    for i,j in my_index.items():
        res.insert(j,i)
 
    print(''.join(res))

reverse_me("Int@Fin^eg#")