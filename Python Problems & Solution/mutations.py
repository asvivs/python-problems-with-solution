# Read a given string, change the character at a given index and then print the modified string.

def fun(user_str, ind, val):
    l1 = list(user_str)
    l1[int(ind)] = val
    return "".join(l1)


user_str = input()
ind, val = input().split()
new_str = fun(user_str, ind, val)
print(new_str)
