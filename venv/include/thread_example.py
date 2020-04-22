from threading import Thread
from concurrent.futures import ThreadPoolExecutor, as_completed


# Thread creating
# 1.1
def f(name):
    print("Hi,", name)


th = Thread(target=f, args=('Jane',))
th.start()
th.join()


# 1.2
class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("Hello,", self.name)


th1 = PrintThread("David")
th1.start()
th.join()


# Thread pool concurrent.futures.Future
# 2.0
def squared_numb(numb_val):
    return numb_val * numb_val


# .shutdown() in exit
with ThreadPoolExecutor(max_workers=3) as pool:
    results = [pool.submit(squared_numb, numb) for numb in range(5)]

    for future in as_completed(results):
        print(future.result())
