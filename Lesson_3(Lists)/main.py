list = [1, 2, 3, 4, 5]
new_list = list[:]  # copy list
print(new_list)

new_list[0:3] = [3, 2, 1]  # replace values
print(new_list)

new_list[:] = []  # clear list
print(new_list)

new_list.append(354)  # added new value
print(new_list)

list = [[1, 2, 3], ['a', 'b', 'c']]  # nested lists - ВЛОЖЕННЫЕ СПИСКИ
print(list[0])
print(list[1][1])

a, b = 0, 1  # multiple assignment - множественное присваивание
while a < 10:
    print(a, end='->')
    a, b = b, a + b
