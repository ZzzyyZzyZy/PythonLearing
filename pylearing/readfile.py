f = open("/Users/zhangyu/Desktop/未命名.txt",'a+')
f.write('Hello, world!')
b = open("/Users/zhangyu/Desktop/未命名.txt",'r')
for line in b.readlines():
    print(line.strip())