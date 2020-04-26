import socket


# Server
with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        conn.settimeout(5)
        with conn:
            while True:
                try:
                    data = conn.recv(1024)
                except socket.timeout:
                    print("close connection by timeout")
                    break
                if not data:
                    break
                print(data.decode("utf8"))


# Client
with socket.create_connection(("127.0.0.1", 10001), 5) as sock1:
    # set socket read timeout
    sock1.settimeout(2)
    try:
        sock.sendall("ping".encode("utf8"))
    except socket.timeout:
        print("send data timeout")
    except socket.error as ex:
        print("send data error:", ex)
