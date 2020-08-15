import multiprocessing
import time

start = time.perf_counter()

def sleep_fn():
    print(f'Sleeping 1 second')
    time.sleep(1)
    print(f'Done Sleeping')

if __name__ == '__main__':
    processes = []

    for _ in range(20):     # an "_" since we won't be using the variable anywhere
        p = multiprocessing.Process(target = sleep_fn)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'finished in {round(finish-start, 2)} seconds(s)')