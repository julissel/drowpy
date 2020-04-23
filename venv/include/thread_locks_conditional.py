import threading

# 1  - "Race condition"


class Point:
    def __init__(self, x, y):
        self.set(x, y)

    def get(self):
        return (self.x, self.y)

    def set(self, x, y):
        self.x = x
        self.y = y


my_point = Point(10, 20)
my_point.get()
my_point.set(15, 12)
my_point.get()


# 2.1  - "Thread synchronization. Locks without context manager"

a = threading.RLock()
b = threading.RLock()

def foo():
    try:
        # acquire - get Lock
        a.acquire()
        b.acquire()
    finally:
        # release - free Lock
        b.release()
        a.release()


# 2.2  - "Thread synchronization. Locks with context manager"


class PointNew:
    def __init__(self, x, y):
        self.mutex = threading.RLock()
        self.set(x, y)

    def get(self):
        with self.mutex:
            return (self.x, self.y)

    def set(self, x, y):
        with self.mutex:
            self.x = x
            self.y = y


new_point = PointNew(11, 22)
new_point.get()
new_point.set(13, 14)
new_point.get()


# 3  - "Conditional variables"


class MyQueue:
    def __init__(self, size=5):
        self._size = size
        self._queue = []
        self._mutex = threading.RLock()
        self._empty = threading.Condition(self._mutex)
        self._full = threading.Condition(self._mutex)

    def put(self, val):
        with self._full:
            while len(self._queue) >= self._size:
                self._full.wait()

            self._queue.append(val)
            self._empty.notify()

    def get(self):
        with self._empty:
            while len(self._queue) == 0:
                self._empty.wait()

            ret = self._queue.pop(0)
            self._full.notify()
            return ret
