from queue import Queue
from threading import Thread


def worker(queue_obj, queue_numb):
    while True:
        item = queue_obj.get()
        if item is None:
            break
        print('process data:  thread #', queue_numb, 'value=', item)


# start queues
que = Queue(5)

# start threads
thr1 = Thread(target=worker, args=(que, 1))
thr2 = Thread(target=worker, args=(que, 2))
thr1.start()
thr2.start()

# generate values
for i in range(25):
    que.put(i)

# stop queues
que.put(None)
que.put(None)

# stop threads
thr1.join()
thr2.join()
