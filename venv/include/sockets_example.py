import socket

# 1 -  using sockets without context manager

# Server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 10001))
sock.listen(socket.SOMAXCONN)

conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    # process data
    print(data.decode("utf8"))

conn.close()
sock.close()


# Client # 01
sock1 = socket.socket()
sock1.connect(("127.0.0.1", 10001))
sock1.sendall("test ping_1".encode("utf8"))
sock1.close()

# Client # 02
sock2 = socket.create_connection(("127.0.0.1", 10001))
sock2.sendall("test ping_2".encode("utf8"))
sock2.close()


# 2 -  using sockets with context manager

# Server
with socket.socket() as sock3:
    sock3.bind(("", 10001))
    sock3.listen()

    while True:
        conn, addr = sock3.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode("utf8"))


# Client
with socket.create_connection(("127.0.0.1", 10001), 5) as sock4:
    sock4.sendall("test ping_3".encode("utf8"))
