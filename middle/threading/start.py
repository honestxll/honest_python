import threading

def thread_job():
  print('This is an added Thread, number is %s'% threading.current_thread())

def main():
  add_thread = threading.Thread(target = thread_job)
  add_thread.start()

  print(threading.active_count())
  print(threading.enumerate())
  print(threading.current_thread())

if __name__ == '__main__':
  main()
