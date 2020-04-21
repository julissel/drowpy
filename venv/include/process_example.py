import time
import os
from multiprocessing import Process


class PrintProcess(Process):
    # using redefinition of method run (inheritance from multiprocessing.Process)
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("Hi,", self.name)


pr = PrintProcess("Alex")
pr.start()
pr.join()


# using multiprocessing
def f(name):
    print("Hello", name)

proc = Process(target=f, args=("Kate",))
proc.start()  # fork to create child process
proc.join()  # finish child process


# generate new child process
pid = os.fork()
tmp_var = "val_0"

if pid == 0:
    # child process
    for i in range(10):
        tmp_var = f"val_{str(i)}"
        print("child: ", os.getpid(), "tmp value = ", tmp_var)
        time.sleep(5)
    time.sleep(5)
else:
    # parent process
    print("parent: ", os.getpid(), "tmp value = ", tmp_var)
    os.wait()
