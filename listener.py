import socket
import simplejson as json


class Listener:

    def __init__(self, ip, port):
        link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        link.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        link.bind((ip, port))
        link.listen(0)
        print('Listening on port {}'.format(port))

        (self.link_1, address) = link.accept()

    def packeting(self, data):
        packet = json.dumps(data)
        self.link_1.sendall(packet.encode("utf-8"))

    def packet_decode(self):
        incoming_data = ""
        while True:
            try:
                incoming_data = incoming_data + self.link_1.recv(1024).decode("utf-8")
                return json.loads(incoming_data)
            except ValueError:
                continue

    def start(self):
        while True:
            entrance = input("Write a command: ")
            self.packeting(entrance)
            output = self.packet_decode()
            print(output)


listener = Listener(ip="127.0.0.1", port=8080)
listener.start()
