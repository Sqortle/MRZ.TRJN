import socket


class Listener:

    def __init__(self, ip, port):
        link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        link.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        link.bind((ip, port))
        link.listen(0)
        print('Listening on port {}'.format(port))

        (self.link_1, address) = link.accept()

    def start(self):
        while True:
            entrance = input("Write a command: ")
            self.link_1.sendall(entrance.encode("utf-8"))
            incoming_data = self.link_1.recv(1024).decode("utf-8")
            print(incoming_data)


listener = Listener(ip="127.0.0.1", port=8080)
listener.start()
