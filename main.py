import hashlib
import multiprocessing
import string
import threading
from sys import argv
from time import time
from itertools import product
import codecs
from multiprocessing import Pool as ThreadPool, Pool

hashes = []
cartesian = list(product(string.ascii_lowercase, repeat=5))
file1 = open('foo.txt', 'r')
lines = file1.readlines()
for line in lines:
    hashes.append(bytes().fromhex(line))
parts = []


def sha(cart):
    for attempt in cart:
        hashed = hashlib.sha256(''.join(attempt).encode("Utf8")).digest()
        if hashed in hashes:
            hashes.remove(hashed)
            print(''.join(attempt))
            if len(hashes) == 0:
                return


if __name__ == "__main__":
    thread_count = int(argv[1])
    step = int(11881376 / thread_count)
    for i in range(thread_count):
        parts.append(cartesian[step * i:step * (i + 1)])
    threads = []
    timer_start = time()
    with multiprocessing.Pool(processes=thread_count) as p:
        p.map(sha, parts)
    # for i in range(thread_count):
    #     t = threading.Thread(target=sha, args=(parts[i], i))
    #     t.start()
    #     threads.append(t)
    # for t in threads:
    #     t.join()
    time_end = time() - timer_start
    print(time_end)
