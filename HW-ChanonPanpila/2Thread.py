# Thread By Chanon Panpila Example ::
import os

from multiprocessing import Process, Queue
from itertools import repeat
import time


def sumArray(arraySet, q):
    print(sum(arraySet))
    t0 = time.time()
    q.put(sum(arraySet))
    t = time.time()
    proc = os.getpid()
    print('Calculate Time for Each Thread : %2.9f' % (t-t0))
    print('Process id', proc)
    time.sleep(1)

# use Double-Thread for seperate task from [4][1000000] by half [4][500000] each


arraySet1 = list(repeat(4, 500000))
arraySet1_1 = list(repeat(4, 500000))

arraySet2 = list(repeat(8, 500000))
arraySet2_1 = list(repeat(8, 500000))

arraySet3 = list(repeat(16, 500000))
arraySet3_1 = list(repeat(16, 500000))

if __name__ == '__main__':

    # try ArraySet 1 / ArraySet 3 / ArraySet 3 : just change
    example1 = [arraySet1, arraySet1_1]
    # example1 = [arraySet1, arraySet1_1] #uncomment this for ArraySet 2 [8][1000000]
    # example1 = [arraySet1, arraySet1_1] #uncomment this for ArraySet 3 [16][1000000]

    procs_ex1 = []
    result1 = 0

    print("2 Thread : 50% task/each")

    t0 = time.time()
    q = Queue()
    for index, number in enumerate(example1):
        proc = Process(target=sumArray, args=(number, q))
        procs_ex1.append(proc)
        proc.start()

    for proc in procs_ex1:
        # print(q.get())
        result1 += q.get()
        proc.join()
    t = time.time()

    print("--- final Result ---")
    print("=", result1)
    print("Overall-Time Rate : %2.9f" % (t-t0))

    print(" ")
    input('press any key to exit...')
