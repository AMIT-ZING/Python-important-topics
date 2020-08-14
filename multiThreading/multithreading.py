import threading
import time

start = time.perf_counter()

def sleep_fn():
    print(f'Sleeping 1 second')
    time.sleep(1)
    print(f'Done Sleeping')

threads = []

for _ in range(20):     # an "_" since we won't be using the variable anywhere
    t = threading.Thread(target = sleep_fn)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'finished in {round(finish-start, 2)} seconds(s)' )

