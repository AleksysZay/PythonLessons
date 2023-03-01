string = 'string'
print(string)
print(string + ' = string')  # string = string

string = 'str' 'ing'
print(string)  # string

string = ('hello'
          ' world'
          ' python')
print(string)  # hello world python

string = '''the
    interesting
                text'''
print(string)
'''
print

the
    interesting
                text
'''

string = 'string'
print(string[0])  # s
print(string[1])  # t
print(string[2])  # r
print(string[3])  # i
print(string[4])  # n
print(string[5])  # g

print(string[-1])  # g
print(string[-2])  # n
print(string[-3])  # i
print(string[-4])  # r
print(string[-5])  # t
print(string[-6])  # s

print(len(string))  # 6
# string[1] = 't'
'''
    TypeError: 'str' object does not support item assignment
'''

print(string[0:3])  # str
print(string[0:])  # string
print(string[:4])  # stri
