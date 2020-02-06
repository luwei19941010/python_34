#-*-coding:utf-8-*-
# Author:Lu Wei
from threading import Thread
import os,time
def func(i):
    print(i,'aaaa',os.getpid())
    time.sleep(1)
    print(i,'end')
t_l=[]
for i in range(10):
    t=Thread(target=func,args=(i,))
    t.start()
    t_l.append(t)
for t in t_l:
    t.join()

print('-->',os.getpid())