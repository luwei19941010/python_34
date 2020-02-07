#-*-coding:utf-8-*-
# Author:Lu Wei
import time
import random
from multiprocessing import JoinableQueue,Process

def producer(q,name,food):
    for i in range(10):
        time.sleep(random.random())
        fd = '%s%s'%(food,i)
        q.put(fd)
        print('%s生产了一个%s'%(name,food))
    q.join()

def consumer(q,name):
    while True:
        food = q.get()
        time.sleep(random.random())
        print('%s吃了%s'%(name,food))
        q.task_done()

if __name__ == '__main__':
    jq = JoinableQueue()
    p =Process(target=producer,args=(jq,'wusir','泔水'))
    p.start()
    c = Process(target=consumer,args=(jq,'alex'))
    c.daemon = True
    c.start()
    p.join()