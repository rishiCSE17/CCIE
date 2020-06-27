# race condition
import threading
import matplotlib.pyplot as plt
import random
import time

shared_counter = 0
lock = threading.Lock()


def th_count(n, sync):
    '''
        get n as integer and adds sequenctially
        to shared counter in a loop
    '''
    global shared_counter
    global lock
    name = threading.current_thread().getName()
    while n > 0:
        if sync:
            lock.acquire()
            shared_counter += 1
            lock.release()
        else:
            shared_counter += 1
        n -= 1
    # print(f'\t{name} done!')


def caller(n, m, sync):
    '''
        crates, run and destry m threads
        each adds n to the shared_counter
        returns the final value of the counter
    '''
    global shared_counter
    shared_counter = 0
    names = [f'th_{j}' for j in range(1, m + 1)]  # names th_1...th_m
    # print(f'count = {shared_counter}')
    for i in range(len(names)):
        if sync == True:
            t = threading.Thread(name=names[i],
                                 target=th_count,
                                 args=(n, True))
        else:
            t = threading.Thread(name=names[i],
                                 target=th_count,
                                 args=(n, False))
        t.start()
    # print(f'count = {shared_counter}')
    return shared_counter


def main():
    '''
        calls the caller funtion for a range of numbers to add
        and numbers of threads
        gets the deviation between expected and computed data and
        plots it
    '''

    import math
    # deviations
    x = []
    dev_y = []
    dev_y_sync = []
    m = 2  # number of threads
    print('calculating...')
    for i in range(10, pow(10, 5), pow(10, 3)):
        global shared_counter
        shared_counter = 0

        x.append(i)
        dev_y.append(math.sqrt(
            pow((m * i) - caller(i, m, sync=False), 2))
        )
        dev_y_sync.append(math.sqrt(
            pow((m * i) - caller(i, m, sync=True), 2))
        )
    # plt.yscale('log')
    plt.plot(x, dev_y, 'r', label='without sync');
    plt.plot(x, dev_y_sync, 'g', label='with sync');
    plt.legend()
    plt.show()