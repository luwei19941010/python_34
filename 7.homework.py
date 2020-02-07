#-*-coding:utf-8-*-
# Author:Lu Wei
# g1 = filter(lambda n:n%2==0,range(10))#2,4,6,8
# g2 = map(lambda n:n*2,range(3))#0,2,4,6
# for i in g1:
#     print('-->',i)
#     for j in g2:
#         print(j)
#         # print(i*j)


def multipliers():
    return (lambda x:i*x for i in range(4))#0,1,2,3
for m in multipliers():
    print(m)
# print([m(2) for m in multipliers()])