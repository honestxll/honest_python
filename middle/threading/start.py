import threading
import time


def thread_job1():
    print('This is an added Thread 1, number is %s \n' %
          threading.current_thread())
    for i in range(10):
        print('T1', i)
    print('T1 finish\n')


def thread_job2():
    for i in range(10):
        print('T2', i)
    print('T2 finish\n')


def main():
    thread1 = threading.Thread(target=thread_job1)
    thread2 = threading.Thread(target=thread_job2)

    thread1.start()
    # 如果想让 T1 这个线程执行完之后再执行下面的代码，可以用 join
    # join 相当于增加了线程的优先级
    # thread1.join()
    thread2.start()
    print('done \n')

    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())


if __name__ == '__main__':
    main()
