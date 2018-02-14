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

# use Quadra-Thread for seperating task from [4][1000000] by 1/4 [4][250000] each


arraySet1 = list(repeat(4, 250000))
arraySet1_1 = list(repeat(4, 250000))
arraySet1_2 = list(repeat(4, 250000))
arraySet1_3 = list(repeat(4, 250000))

arraySet2 = list(repeat(8, 250000))
arraySet2_1 = list(repeat(8, 250000))
arraySet2_2 = list(repeat(8, 250000))
arraySet2_3 = list(repeat(8, 250000))

arraySet3 = list(repeat(16, 250000))
arraySet3_1 = list(repeat(16, 250000))
arraySet3_2 = list(repeat(16, 250000))
arraySet3_3 = list(repeat(16, 250000))


if __name__ == '__main__':

    # try ArraySet 1 / ArraySet 3 / ArraySet 3 : just change
    example1 = [arraySet1, arraySet1_1, arraySet1_2, arraySet1_3]
    #example1 = [arraySet2, arraySet2_1, arraySet2_2,arraySet2_3]
    #example1 = [arraySet3, arraySet3_1, arraySet3_2,arraySet3_3]

    procs_ex1 = []
    result1 = 0

    print("4 Thread : 25% task each")

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
