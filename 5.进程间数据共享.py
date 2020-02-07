#-*-coding:utf-8-*-
# Author:Lu Wei
from multiprocessing import Process,Manager,Lock

def func(dic,l):
    with l:
        dic['count']-=1

if __name__ == '__main__':
    m=Manager()
    l=Lock()
    dic=m.dict({'count':100})
    p_l=[]
    for i in range(10):
        p=Process(target=func,args=(dic,l))
        p.start()
        p_l.append(p)
    for p in p_l:p.join()
    print(dic)