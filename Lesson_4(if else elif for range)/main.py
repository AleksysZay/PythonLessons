# if
x = int(input('enter digit: '))
if x < 0:
    print('<0')
elif x == 0:
    print('=0')
else:
    print('>0')

# for
list = ['abcd', 'if', 'ghi', 'gkl']
for i in list:
    print(i, len(i))

# range
for i in range(5, 10, 2):
    print(i)