L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
print(L[:3])

# range(100) 从0开始到99 不包含100
print(list(range(100)))

print(list(range(100))[2:10])

print(list(range(100))[:10:2])

print(list(range(100))[::2])


# -*- coding: utf-8 -*-

# 完整版

def trim(s):
    while s[:1] == ' ' or s[-1:] == ' ':

        if s[:1] == ' ':
            s_len = len(s)

            s = s[-(s_len - 1):]

        if s[-1:] == ' ':
            s_len = len(s)

            s = s[:s_len - 1]

    return s


# 测试:

if trim('hello  ') != 'hello':

    print('测试失败1!')

elif trim('  hello') != 'hello':

    print('测试失败2!')

elif trim('  hello  ') != 'hello':

    print('测试失败3!')

elif trim('  hello  world  ') != 'hello  world':

    print('测试失败4!')

elif trim('') != '':

    print('测试失败5!')

elif trim('    ') != '':

    print('测试失败6!')

else:

    print('测试成功!')
