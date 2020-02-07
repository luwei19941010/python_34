#-*-coding:utf-8-*-
# Author:Lu Wei
from multiprocessing import Queue,Process
import random
import time



def producer(q,name,food):
    for i in range(10):
        time.sleep(random.random())
        q.put('%s%s'%(food,i))
        print('%s生产了一个%s'%(name,food))

def consumer(q,name):
    while True:
        food = q.get()
        if not food:break
        time.sleep(random.random())
        print('%s吃了%s'%(name,food))

def cp(c_num,p_num):
    q=Queue()
    for i in range(c_num):
        Process(target=consumer,args=(q,'alex')).start()
    p_l=[]
    for i in range(p_num):
        p=Process(target=producer,args=(q,'wusir','泔水'))
        p.start()
        p_l.append(p)
    for p in p_l:p.join()
    for i in range(c_num):q.put(None)
if __name__ == '__main__':
    cp(2,3)
























#
# def producer(q,name,food):
#     for i in range(10):
#         time.sleep(random.random())
#         fd='%s%s'%(food,i)
#         q.put(fd)
#         print('%s生产了一个%s'%(name,food))
#
# def consumer(q,name):
#     while True:
#         food=q.get()
#         if not food :break
#         time.sleep(random.randint(1,3))
#         print('%s吃了%s'%(name,food,))
#
# def cp(c_num,p_num):
#     q=Queue(3)
#     for i in range(c_num):
#         Process(target=consumer,args=(q,'alex',)).start()
#     p_l=[]
#     for i in range(p_num):
#         p=Process(target=producer,args=(q,'wusir','泔水'))
#         p.start()
#         p_l.append(p)
#     for p in p_l:p.join()
#     for i in range(c_num):
#         q.put(None)
# if __name__ == '__main__':
#     cp(2,1)

