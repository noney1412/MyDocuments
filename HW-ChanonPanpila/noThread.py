from itertools import repeat
import time


arraySet1 = list(repeat(4, 1000000))
arraySet2 = list(repeat(8, 1000000))
arraySet3 = list(repeat(16, 1000000))


def NoThread(arraySet):
    t0 = time.time()
    print(sum(arraySet))
    t = time.time()
    print('Time Rate : %2.9f' % (t-t0))
    time.sleep(2)


NoThread(arraySet1)
NoThread(arraySet2)
NoThread(arraySet3)

print(" ")
input('press any key to exit...')
