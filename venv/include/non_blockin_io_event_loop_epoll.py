import socket
import select


sock = socket.socket()
sock.bind(("", 10001))
sock.listen()

conn1, addr = sock.accept()
conn2, addr = sock.accept()

# set the connection to non-blocking mode
conn1.setblocking(0)
conn2.setblocking(0)

epoll = select.epoll()

# file-descriptors, subscribe with mask for read | for write
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2,
}

# event-loop in epoll
while True:
    # system call
    events = epoll.poll(1)
    # contains file-descriptor and its event
    for fileno, event in events:
        if event & select.EPOLLIN:
            # read
            data = conn_map[fileno].recv(1024)
            print(data.decode("utf8"))
        elif event & select.EPOLLOUT:
            # write
            conn_map[fileno].send("ping".encode("utf8"))
