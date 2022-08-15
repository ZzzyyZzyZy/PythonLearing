tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

###列表

tinydict['Age'] = 8  # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息

print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

str = "C语言中文网"
print(str[0], "==", str[-6])
print(str[5], "==", str[-1])

# 序列切片
# 取索引区间为[0,2]之间（不包括索引2处的字符）的字符串
print(str[:2])
# 隔 1 个字符取一个字符，区间是整个字符串
print(str[::2])
# 取整个字符串，此时 [] 中只需一个冒号即可
print(str[:])

# 列表的创建用 []，后续讲解列表时会详细介绍
list = [None] * 5
print(list)

str = "c.biancheng.net"
print('c' in str)

str = "c.biancheng.net"
print('c' not in str)

print(len(str))
print(min(str))
print(sorted(str))

list = ['Google', 'Runoob', 1997, 2000]

print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])

list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print("更新后的列表 : ", list1)

list = ['Google', 'Runoob', 1997, 2000]

print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)

import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a, b))
print("operator.eq(c,b): ", operator.eq(c, b))

### 元组
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

# 修改元组
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 字典
# 使用大括号 {} 来创建空字典
emptyDict = {}

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])

# print ("tinydict['Alice']: ", tinydict['Alice'])

tinydict['Age'] = 8  # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息

print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])

del tinydict['Name']  # 删除键 'Name'
tinydict.clear()  # 清空字典
del tinydict  # 删除字典

# 集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)

a = {x for x in 'abracadabraeg' if x not in 'abc'}
print(a)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)

thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1,3})
print(thisset)

thisset.update([1,4],[5,6])
print(thisset)


thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset)


thisset = set(("Google", "Runoob", "Taobao"))
thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)

thisset1 = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset1.pop()

print(x)
print(len(thisset1))

thisset = set(("Google", "Runoob", "Taobao"))
thisset.clear()
print(thisset)


a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b


list=[1,2,34,4,3]
it = iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

import sys  # 引入 sys 模块

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()


# 字典创建方式
d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
print(d1 == d2 == d3 ==d4)

# 集合创建方式
s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(s1 == s2)


