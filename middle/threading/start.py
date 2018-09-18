import threading
import time

def thread_job():
  print('This is an added Thread 1, number is %s \n'% threading.current_thread())
  for i in range(10):
    time.sleep(0.1)
  print('T1 finish\n')

def main():
  add_thread = threading.Thread(target = thread_job)
  add_thread.start()
  print('done \n')

  print(threading.active_count())
  print(threading.enumerate())
  print(threading.current_thread())

if __name__ == '__main__':
  main()
