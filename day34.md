### day34

#### 今日内容

#### 1.生产者消费者模型

```
#producer
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

```

#### 2.jion able queue

![](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200205190817846.png)

```
#JoinableQueue
import time
import random
from multiprocessing import JoinableQueue,Process

def producer(q,name,food):
    for i in range(10):
        time.sleep(random.random())
        fd = '%s%s'%(food,i)
        q.put(fd)
        print('%s生产了一个%s'%(name,food))
    q.join()			#等待q对象结束，当q对象中count值为0时结束

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
    c.daemon = True		#将消费者设置为保护进程，随着主进程代码结束而结束
    c.start()	
    p.join()		   #等待生产进程结束
```

![image-20200205191942038](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200205191942038.png)



#### 3.进程间数据共享Manager()

```
# mulprocessing中有一个manager类
# 封装了所有和进程相关的 数据共享 数据传递
# 相关的数据类型
# 但是对于 字典 列表这一类的数据操作的时候会产生数据不安全
# 需要加锁解决问题，并且需要尽量少的使用这种方式

from multiprocessing import Manager,Process,Lock

def func(dic,lock):
    with lock:				#由于数据共享，就存在多个进程会同时操作数据的情况，所以需要加锁来确保数据安全性
        dic['count'] -= 1

if __name__ == '__main__':
    # m = Manager()
    with Manager() as m:
        l = Lock()
        dic = m.dict({'count':100})
        p_l = []
        for i in range(100):
            p = Process(target=func,args=(dic,l))
            p.start()
            p_l.append(p)
        for p in p_l:p.join()
        print(dic)
```

#### 4.线程

- 线程 开销小 数据共享 是进程的一部分

- 进程 开销大 数据隔离 是一个资源分配单位

- cpython解释器 不能实现多线程利用多核（由于python的垃圾回收机制造成）

  - python对不在使用的资源会由某一线程进行回收。

  - 回收资源线程通过对程序中变量统计引用计数

    #会存在这种情况，当线程A与线程B都有（a=1)时，线程A执行完成之后，被线程C（回收资源线程）感知到，线程C则去处理引用计算器减法，在C线程进行计算的时候，B进程执行（a=1）完成之后。这时候就会存在C线程无法感知到B现场处理完成。最终导致资源无法正常回收

    

![image-20200205221527286](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200205221527286.png)

```
# 锁 ：GIL 全局解释器锁
    # 保证了整个python程序中，只能有一个线程被CPU执行
    # 原因：cpython解释器中特殊的垃圾回收机制
    # GIL锁导致了线程不能并行，可以并发
# 所以使用所线程并不影响高io型的操作
# 只会对高计算型的程序由效率上的影响
# 遇到高计算 ： 多进程 + 多线程
              # 分布式

# cpython pypy jpython iron python

# 遇到IO操作的时候
    # 5亿条cpu指令/s
    # 5-6cpu指令 == 一句python代码
    # 几千万条python代码
# web框架 几乎都是多线程
```

##### 4.1 守护线程

```
# 守护线程一直等到所有的非守护线程都结束之后才结束
# 除了守护了主线程的代码之外也会守护子线程
import time
from threading import Thread
def son1():
    while True:
        time.sleep(0.5)
        print('in son1')
def son2():
    for i in range(5):
        time.sleep(1)
        print('in son2')
t =Thread(target=son1)
t.daemon = True
t.start()
Thread(target=son2).start()
time.sleep(3)
```

##### 4.2 开启多个子线程

```
# 开启多个子线程
# def func(i):
#     print('start son thread',i)
#     time.sleep(1)
#     print('end son thread',i,os.getpid())
#
# for i in range(10):
#     Thread(target=func,args=(i,)).start()
# print('main')
# 主线程什么时候结束？等待所有子线程结束之后才结束
# 主线程如果结束了，主进程也就结束了
```

##### 4.3 join方法

```
# join方法  阻塞 直到子线程执行结束
# def func(i):
#     print('start son thread', i)
#     time.sleep(1)
#     print('end son thread', i, os.getpid())
#
#
# t_l = []
# for i in range(10):
#     t = Thread(target=func, args=(i,))
#     t.start()
#     t_l.append(t)
# for t in t_l: t.join()
# print('子线程执行完毕')
```

##### 4.4使用面向对象开启子线程

```
# 使用面向对象的方式启动线程
# class MyThread(Thread):
#     def __init__(self, i):
#         self.i = i
#         super().__init__()
#
#     def run(self):
#         print('start', self.i, self.ident)
#         time.sleep(1)
#         print('end', self.i)
#
#
# for i in range(10):
#     t = MyThread(i)
#     t.start()
#     print(t.ident)
```



##### 4.5 线程 active_count/current_thread/enumerate

```
# 线程里的一些其他方法
# from threading import current_thread,enumerate,active_count
# def func(i):
#     t = current_thread()
#     print('start son thread',i,t.ident)
#     time.sleep(1)
#     print('end son thread',i,os.getpid())
#
# t = Thread(target=func,args=(1,))
# t.start()
# print(t.ident)
# print(current_thread().ident)   # 水性杨花 在哪一个线程里，current_thread()得到的就是这个当前线程的信息
# print(enumerate())		#有多少在运行的线程
# print(active_count())   # =====len(enumerate())

# terminate 结束进程
# 在线程中不能从主线程结束一个子线程
```



#### 

