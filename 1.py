#-*-coding:utf-8-*-
# Author:Lu Wei

# def demo():
#     for i in range(4):
#         yield i
#
# d=demo()
# d1=(i for i in  d)
# d2=(i for i in d1)
# print(list(d1)) #从这里开始取值
# print(list(d2))

def  add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i

g=test()
for n in [1,10]:
    g=(add(n,i) for i in g )
    print(list(g))
print(list(g))

