import threading
import time

# create a flag to control the thread's execution
stop_thread = False


def worker():
    while not stop_thread:
        print("Thread is running...")
        time.sleep(1)
        print("Thread is stopping...")


# create and start the thread
thread = threading.Thread(target=worker)
thread.start()

# let the thread run for five seconds
time.sleep(5)

# signal the thread to stop
stop_thread = True

# wait for the thread to finish
thread.join()
print("Thread has terminated.")