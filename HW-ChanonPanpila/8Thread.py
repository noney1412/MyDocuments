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

# use Eight-Thread for seperating task from [4][1000000] by 1/8 [4][125000] each


arraySet1 = list(repeat(4, 125000))
arraySet1_1 = list(repeat(4, 125000))
arraySet1_2 = list(repeat(4, 125000))
arraySet1_3 = list(repeat(4, 125000))
arraySet1_4 = list(repeat(4, 125000))
arraySet1_5 = list(repeat(4, 125000))
arraySet1_6 = list(repeat(4, 125000))
arraySet1_7 = list(repeat(4, 125000))

arraySet2 = list(repeat(8, 125000))
arraySet2_1 = list(repeat(8, 125000))
arraySet2_2 = list(repeat(8, 125000))
arraySet2_3 = list(repeat(8, 125000))
arraySet2_4 = list(repeat(8, 125000))
arraySet2_5 = list(repeat(8, 125000))
arraySet2_6 = list(repeat(8, 125000))
arraySet2_7 = list(repeat(8, 125000))

arraySet3 = list(repeat(16, 125000))
arraySet3_1 = list(repeat(16, 125000))
arraySet3_2 = list(repeat(16, 125000))
arraySet3_3 = list(repeat(16, 125000))
arraySet3_4 = list(repeat(16, 125000))
arraySet3_5 = list(repeat(16, 125000))
arraySet3_6 = list(repeat(16, 125000))
arraySet3_7 = list(repeat(16, 125000))


if __name__ == '__main__':

    # try ArraySet 1 / ArraySet 3 / ArraySet 3 : just change
    example1 = [arraySet1, arraySet1_1, arraySet1_2, arraySet1_3,
                arraySet1_4, arraySet1_5, arraySet1_6, arraySet1_7]
    # example1 = [arraySet2, arraySet2_1, arraySet2_2, arraySet2_3,
    #             arraySet2_4, arraySet2_5, arraySet2_6, arraySet2_7]
    # example1 = [arraySet3, arraySet3_1, arraySet3_2, arraySet3_3,
    #             arraySet3_4, arraySet3_5, arraySet3_6, arraySet3_7]
    

    procs_ex1 = []
    result1 = 0

    print("8 Thread : 12.5% task each")

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
