import os
import socket
import threading
import _multiprocessing


# 1
# few connections
with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        print("connected client:", addr)
        # process for connection processing
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode("utf8"))


# 2
# Threads. Processing several connections
def process_request(conn, addr):
    print("connectioed cclient:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))

with socket.socket() as sock1:
    sock1.bind(("", 10001))
    sock1.listen()
    while true:
        conn, addr = sock1.accept()
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()


# 3
# Processes and Threads. Processing several connections

# 3.1
with socket.socket() as sock2:
    sock2.bind(("", 10001))
    sock2.listen()
    # create several processes
    while True:
        conn, addr = sock2.accept()
        # thread for coonection processing
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode("utf8"))


# 3.2
with socket.socket() as sock3:
    sock3.bind(("", 10001))
    sock3.listen()

    workers_count = 3
    workers_list = [multiprocessing.Process(target=workers, args=(sock3,)) for _ in range(workers_count)]

    for w in workers_list:
        w.start()

    for w in workers_list:
        w.join()


# 3.3
def worker(sock):
    while True:
        conn, addr = sock.accept()
        print("pid", os.getpid())
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()

def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))
