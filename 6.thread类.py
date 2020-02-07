#-*-coding:utf-8-*-
# Author:Lu Wei

# 守护线程
# import time,os
# from threading import Thread
# def son1():
#     while True:
#         time.sleep(0.5)
#         print('in son1')
# def son2():
#     for i in range(5):
#         time.sleep(1)
#         print('in son2')
# t =Thread(target=son1)
# t.daemon = True
# t.start()
# Thread(target=son2).start()
# time.sleep(3)
# 守护线程一直等到所有的非守护线程都结束之后才结束
# 除了守护了主线程的代码之外也会守护子线程


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
# print(enumerate())
# print(active_count())   # =====len(enumerate())


from threading import Thread,current_thread,active_count,enumerate
import time,os


def func(i):
    print(current_thread().ident)
    time.sleep(1)
    print(i)

t=Thread(target=func,args=(1,))
t.start()
print(t.ident)
print(enumerate())
print(current_thread().ident)









# terminate 结束进程
# 在线程中不能从主线程结束一个子线程




# def func(i):
#     print(i,'aaaa',os.getpid())
#     time.sleep(1)
#     print(i,'end')
# t_l=[]
# for i in range(10):
#     t=Thread(target=func,args=(i,))
#     t.start()
#     t_l.append(t)
# for t in t_l:
#     t.join()
#
# print('-->',os.getpid())