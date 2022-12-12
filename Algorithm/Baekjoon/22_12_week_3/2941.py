change_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for c in change_lst:
    word = word.replace(c, 'a')
print(len(word))